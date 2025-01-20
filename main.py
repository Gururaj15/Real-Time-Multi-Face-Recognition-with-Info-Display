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

    return image_bgr
