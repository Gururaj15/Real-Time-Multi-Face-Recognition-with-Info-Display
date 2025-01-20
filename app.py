import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import cv2
import face_recognition
import csv
import os

# Load people data from CSV
people_data = {}
with open('people_data.csv', mode='r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        people_data[row['name']] = {
            'country': row['country'],
            'height': row['height'],
            'age': row['age']
        }

# Load images and create face encodings
known_face_encodings = []
known_face_names = []

dataset_path = r'C:\Users\Admin\OneDrive\Desktop\FDI\project\dataset'  # Folder containing images

for filename in os.listdir(dataset_path):
    if filename.endswith(".jpg"):
        # Load the image file
        image = face_recognition.load_image_file(os.path.join(dataset_path, filename))
        encoding = face_recognition.face_encodings(image)
        
        if encoding:
            known_face_encodings.append(encoding[0])
            known_face_names.append(filename.split('.')[0].replace('_', ' '))  # Replace underscores with spaces

# Function to process image and display details
def process_image(image_path):
    # Load the image
    image_bgr = cv2.imread(image_path)
    image_rgb = cv2.cvtColor(image_bgr, cv2.COLOR_BGR2RGB)

    # Find face locations and encodings in the image
    face_locations = face_recognition.face_locations(image_rgb)
    face_encodings = face_recognition.face_encodings(image_rgb, face_locations)

    face_names = []

    for face_encoding in face_encodings:
        matches = face_recognition.compare_faces(known_face_encodings, face_encoding)

        name = "Unknown"

        if True in matches:
            first_match_index = matches.index(True)
            name = known_face_names[first_match_index]

        face_names.append(name)

    # Draw rectangles around faces and display names and details
    for (top, right, bottom, left), name in zip(face_locations, face_names):
        # Draw a rectangle around the face
        cv2.rectangle(image_bgr, (left, top), (right, bottom), (0, 0, 255), 2)

        # Display the name
        cv2.putText(image_bgr, name, (left + 6, top - 6), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 3)

        # Display person's information (larger text size)
        if name != "Unknown":
            person_info = people_data[name]
            info_text = f"Country: {person_info['country']} | Height: {person_info['height']} | Age: {person_info['age']}"
            cv2.putText(image_bgr, info_text, (left + 6, bottom + 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 3)

    # Convert image to RGB for displaying in Tkinter
    image_rgb = cv2.cvtColor(image_bgr, cv2.COLOR_BGR2RGB)
    pil_image = Image.fromarray(image_rgb)
    pil_image = pil_image.resize((800, 600))  # Resize to a larger size for better viewing
    return pil_image

# Function for real-time face detection
def real_time_detection():
    video_capture = cv2.VideoCapture(0)

    while True:
        ret, frame = video_capture.read()
        if not ret:
            break

        # Convert to RGB
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Find face locations and encodings in the frame
        face_locations = face_recognition.face_locations(rgb_frame)
        face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

        face_names = []

        for face_encoding in face_encodings:
            matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
            name = "Unknown"
            if True in matches:
                first_match_index = matches.index(True)
                name = known_face_names[first_match_index]
            face_names.append(name)

        # Draw rectangles and display names on the frame
        for (top, right, bottom, left), name in zip(face_locations, face_names):
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
            cv2.putText(frame, name, (left + 6, top - 6), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 3)

            # Display person's information
            if name != "Unknown":
                person_info = people_data[name]
                info_text = f"Country: {person_info['country']} | Height: {person_info['height']} | Age: {person_info['age']}"
                cv2.putText(frame, info_text, (left + 6, bottom + 30), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 3)

        # Convert the frame to an image for Tkinter
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        pil_image = Image.fromarray(rgb_frame)
        pil_image = pil_image.resize((800, 600))  # Resize to a larger size for better viewing

        # Display the image in the GUI
        img = ImageTk.PhotoImage(pil_image)

        # Create the photo image only after the window is initialized
        if not hasattr(real_time_detection, "label"):
            label.config(image=img)
            label.image = img

        # Refresh the window
        window.update()

    video_capture.release()

# Function to upload and process image
def upload_image():
    file_path = filedialog.askopenfilename(title="Select an image", filetypes=[("Image Files", "*.jpg;*.jpeg;*.png")])
    if file_path:
        pil_image = process_image(file_path)
        img = ImageTk.PhotoImage(pil_image)
        label.config(image=img)
        label.image = img

# Tkinter UI setup
window = tk.Tk()
window.title("Face Detection")
window.geometry("900x700")  # Resize the window to make it larger

# Button to upload an image
upload_button = tk.Button(window, text="Upload Image", command=upload_image, width=20, height=2)
upload_button.pack(pady=20)

# Button for real-time webcam detection
real_time_button = tk.Button(window, text="Real-Time Detection", command=real_time_detection, width=20, height=2)
real_time_button.pack(pady=20)

# Label to display the image
label = tk.Label(window)
label.pack(pady=20)

window.mainloop()
