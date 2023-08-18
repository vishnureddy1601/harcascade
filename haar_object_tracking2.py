import numpy as np
import cv2

# Path to the image
img_path = '//Documents//Finalproject//photos//men.jpg'

# Load the image
img = cv2.imread(img_path)

# Check if the image was loaded successfully
if img is None:
    print("Error: Unable to load image.")
else:
    print("Image loaded successfully!")

# Check the number of channels in the loaded image
num_channels = img.shape[2]
if num_channels == 3:  # BGR image
    # Convert the image to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.imshow('Grayscale Image', gray)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
elif num_channels == 1:  # Grayscale image
    print("Image is already in grayscale format.")
else:
    print("Unsupported image format.")
