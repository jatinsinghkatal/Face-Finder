
# Face Recognition Web App

This project is a web-based face recognition application built using JavaScript for the front end and Python (Flask) for the back end. Users can upload an image, and the system will search through known images for a potential match. If a match is found, the matching image is displayed along with the result.

## Table of Contents
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Project Structure](#project-structure)
- [Setup Instructions](#setup-instructions)
- [Screenshots](#screenshots)

---

## Features

- **Face Recognition**: Uses the `face_recognition` library to identify matches between uploaded and stored images.
- **Result Notification**: Notifies users if a match is found or not.
- **Image Preview**: Displays both the uploaded and matched images (if found).

---

## Technologies Used

- **Frontend**: HTML, CSS, JavaScript (ES6)
- **Backend**: Python (Flask)
- **Face Recognition**: Python `face_recognition` library
- **Cross-Origin Resource Sharing (CORS)**: Enabled with `flask-cors`

---

## Project Structure
```
Face-Finder-WebApp/
├── static/
│   └── matches/        # Directory for storing known images and returning matched images
├── templates/
│   ├── index.html      # Main HTML file for the web interface
|   ├── styles.css      # CSS file for the frontend styling
│   └── script.js       # JavaScript file for progress handling
├── uploads/            # Temporary directory for uploaded images
├── app.py              # Main Flask application script
├── requirements.txt    # List of required Python packages
└── README.md           # Project documentation
```
---

## Setup Instructions

### Prerequisites

- **Python 3.7+**
- **Flask**: Web framework for Python.
- **face_recognition**: Python library for face recognition.
- **Flask-CORS**: For handling Cross-Origin Resource Sharing (CORS).
- **JavaScript**: For handling progress bar and image preview on the frontend.

### Installation

- Clone the repository:
```
    git clone https://github.com/jatinsinghkatal/Face-Finder
```
- Change into the project directory:
```
    cd Face-Finder
```
- Install the required packages:
```
    pip install -r requirements.txt
``` 
---

## Screenshots

### 1. Upload Form
![Upload Form](https://github.com/jatinsinghkatal/Images_for_Readme/blob/main/Face-Finder/Screenshot%202024-11-12%20011920.png)

### 2. Finding a Match
![Finding a Match](https://github.com/jatinsinghkatal/Images_for_Readme/blob/main/Face-Finder/Screenshot%202024-11-12%20012049.png)

### 3. Match Found
![Match Found](https://github.com/jatinsinghkatal/Images_for_Readme/blob/main/Face-Finder/Screenshot%202024-11-12%20005459.png)

### 4. If No Faces Found

![No Faces Found](https://github.com/jatinsinghkatal/Images_for_Readme/blob/main/Face-Finder/Screenshot%202024-11-12%20012131.png)






