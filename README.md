# Real-Time-Multi-Face-Recognition-with-Info-Display

This project is a Face Recognition Application that uses a webcam or image to detect faces, recognize them, and display the identified person's details (country, height, and age). The application leverages face recognition, computer vision techniques, and a Tkinter GUI for real-time face detection and recognition.

# Features

Real-Time Face Detection: Detects and recognizes multiple faces in real-time using a webcam.
Image Upload and Recognition: Allows users to upload images and displays recognized faces with their associated details.
Face Details Display: Displays personal details like country, height, and age of recognized faces, retrieved from a CSV file.

# Technologies Used

Python 3.x
Tkinter: GUI for the application interface.
OpenCV: For real-time webcam video capture and processing.
Face Recognition: For detecting and recognizing faces in images and videos.
Pillow: For image handling and integration with Tkinter.
CSV: Used for storing personal details related to recognized faces.

# Prerequisites

Before running the project, ensure the following Python libraries are installed:
face_recognition
Pillow
opencv-python
numpy
csv
tkinter

# dataset/ Folder

This folder should contain images of faces used for recognition. The images should be named after the person's name (e.g., John.jpg, Alice.jpg), and these names should match the entries in the people_data.csv file.

# How It Works

Loading Data: The application loads a CSV file (people_data.csv) that contains personal details (country, height, and age) of known people.
Face Encoding: Images of known faces are processed to generate face encodings, which are stored for recognition.

Real-Time Face Recognition:
When the user clicks on the "Real-Time Detection" button, the webcam is activated.
The program continuously captures frames from the webcam, detects faces in the frames, and matches them to the known faces.
Upon recognizing a face, the corresponding details (country, height, age) are displayed alongside the detected face.

Image Upload: Users can also upload an image for face recognition, and the program will display recognized faces with personal details.

# Run the Application

python app.py

# Results

The application recognizes faces in both real-time video and uploaded images.
For each recognized face, the personal details are displayed (country, height, age).
Faces that are not recognized are marked as "Unknown."
