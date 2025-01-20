import os
from PIL import Image
import cv2

# Path to the dataset folder
folder_path = r"C:\Users\Admin\OneDrive\Desktop\FDI\project\dataset"

# Iterate through all images in the folder
for file_name in os.listdir(folder_path):
    if file_name.endswith(('.jpg', '.jpeg', '.png')):  # Consider image formats
        image_path = os.path.join(folder_path, file_name)
        
        try:
            # Open image with PIL to inspect its details
            pil_image = Image.open(image_path)
            print(f"\nInspecting Image: {file_name}")
            print(f"Format: {pil_image.format}")
            print(f"Mode: {pil_image.mode}")
            print(f"Size: {pil_image.size}")
            print(f"Dtype (if accessible): {type(pil_image).__name__}")

            # Load the image with OpenCV for further inspection
            image_array = cv2.imread(image_path)
            print(f"OpenCV Image Details:")
            print(f"Type: {type(image_array)}")
            print(f"Shape: {image_array.shape if image_array is not None else 'Image Not Loaded'}")
            print(f"Dtype: {image_array.dtype if image_array is not None else 'N/A'}")
            
        except Exception as e:
            print(f"Error loading image {file_name}: {e}")
