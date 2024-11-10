import os
from flask import Flask, request, jsonify, send_from_directory, render_template, url_for
import face_recognition
from flask_cors import CORS

# Initialize Flask app
app = Flask(__name__, static_folder='static', template_folder='templates')
CORS(app)

# Folder paths (assuming everything is in fcr/facerecognition)
FC_PROJECT_PATH = os.path.abspath(os.path.dirname(__file__))  # This gives the current directory (fcr/facerecognition)
KNOWN_IMAGES_FOLDER = os.path.join(FC_PROJECT_PATH, 'known_images')  # Path to the known images
UPLOAD_FOLDER = os.path.join(FC_PROJECT_PATH, 'uploads')  # Folder for uploaded images
STATIC_FOLDER = os.path.join(FC_PROJECT_PATH, 'static', 'matches')  # Folder for storing matched images

# Ensure necessary folders exist
os.makedirs(KNOWN_IMAGES_FOLDER, exist_ok=True)
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(STATIC_FOLDER, exist_ok=True)

# Home route to render the HTML page
@app.route('/')
def index():
    return render_template('index.html')

# Upload route to process the image
@app.route('/upload', methods=['POST'])
def upload_image():
    if 'image' not in request.files:
        return jsonify({"error": "No image part"}), 400

    file = request.files['image']
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400

    try:
        file.seek(0)  # Rewind file pointer
        uploaded_image = face_recognition.load_image_file(file)
        uploaded_face_encodings = face_recognition.face_encodings(uploaded_image)

        if not uploaded_face_encodings:
            return jsonify({"error": "No faces found in the uploaded image."}), 400

        match_found = False
        matched_image = ""

        # Loop through all images in the known_images folder to check for matches
        test_image_files = [f for f in os.listdir(KNOWN_IMAGES_FOLDER) if f.endswith(('jpg', 'jpeg', 'png'))]

        for test_image_file in test_image_files:
            test_image_path = os.path.join(KNOWN_IMAGES_FOLDER, test_image_file)
            test_image = face_recognition.load_image_file(test_image_path)
            test_face_encodings = face_recognition.face_encodings(test_image)

            for test_face_encoding in test_face_encodings:
                matches = face_recognition.compare_faces(uploaded_face_encodings, test_face_encoding)
                if True in matches:
                    match_found = True
                    matched_image = test_image_file
                    break  # Exit the loop if a match is found

            if match_found:
                break  # Exit outer loop if a match is found

        if match_found:
            # Return the matched image URL correctly using Flask's url_for
            matched_image_url = url_for('static', filename=f'matches/{matched_image}')
            return jsonify({
                "matchFound": True,
                "matchedImage": matched_image,
                "imageUrl": matched_image_url  # Provide the correct image URL for the frontend
            }), 200
        else:
            return jsonify({"matchFound": False, "message": "No match found."}), 404

    except Exception as e:
        print(f"Error processing the image: {e}")
        return jsonify({"error": f"Error processing the image: {e}"}), 500

# Route for serving matched images
@app.route('/static/matches/<filename>')
def serve_image(filename):
    return send_from_directory(STATIC_FOLDER, filename)

if __name__ == '__main__':
    app.run(debug=True)
