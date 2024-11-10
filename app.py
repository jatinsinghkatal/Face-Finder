import os
from flask import Flask, request, jsonify
import face_recognition
from PIL import Image
import io
from flask_cors import CORS


app = Flask(__name__)
CORS(app)

# Folder containing test images (replace with your folder path)
test_images_folder = 'C:\\Users\\jatin\\FCProject'

@app.route('/upload', methods=['POST'])
def upload_image():
    if 'image' not in request.files:
        return jsonify({"error": "No image part"}), 400

    file = request.files['image']
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400

    try:
        # Rewind the file pointer after reading its size
        file.seek(0)

        # Save the uploaded image temporarily to process
        uploaded_image = face_recognition.load_image_file(file)

        # Find all faces and their encodings in the uploaded image
        uploaded_face_encodings = face_recognition.face_encodings(uploaded_image)

        if not uploaded_face_encodings:
            return jsonify({"error": "No faces found in the uploaded image."}), 400

        # Compare each face in the uploaded image with faces in the images folder
        match_found = False
        matched_image = ""

        # Loop through all images in the folder to check for matches
        test_image_files = [f for f in os.listdir(test_images_folder) if f.endswith(('jpg', 'jpeg', 'png'))]

        for test_image_file in test_image_files:
            test_image_path = os.path.join(test_images_folder, test_image_file)

            # Load the test image and find encodings
            test_image = face_recognition.load_image_file(test_image_path)
            test_face_encodings = face_recognition.face_encodings(test_image)

            # Compare faces
            for test_face_encoding in test_face_encodings:
                matches = face_recognition.compare_faces(uploaded_face_encodings, test_face_encoding)
                if True in matches:
                    match_found = True
                    matched_image = test_image_file
                    break  # Exit the loop if a match is found

            if match_found:
                break  # Exit the loop if a match is found

        if match_found:
            return jsonify({"matchFound": True, "matchedImage": matched_image}), 200
        else:
            return jsonify({"matchFound": False, "message": "No match found."}), 404

    except Exception as e:
        # Log the error for debugging
        print(f"Error processing the image: {e}")
        return jsonify({"error": f"Error processing the image: {e}"}), 500


if __name__ == '__main__':
    app.run(debug=True)
