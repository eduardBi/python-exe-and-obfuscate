import cv2
import numpy as np
import sys
import signal
import os

def add_border_and_show(image_path):
    # Read the image
    image = cv2.imread(image_path)

    if image is None:
        print("Error: Unable to load image.")
        sys.exit(1)

    # Define border size and color (red border)
    border_size = 50
    border_color = (255, 0, 0)  # Red border

    # Add border to the image
    bordered_image = cv2.copyMakeBorder(image, border_size, border_size, border_size, border_size, 
                                        cv2.BORDER_CONSTANT, value=border_color)

    # Display the image with the border
    cv2.imshow("Bordered Image", bordered_image)
    
    # Wait for a key press and close the image window
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # Ensure console exits
    sys.exit(0)

# Handle Ctrl+C properly
def signal_handler(sig, frame):
    print("\nClosing gracefully...")
    cv2.destroyAllWindows()
    sys.exit(0)

# Register signal handler for Ctrl+C
signal.signal(signal.SIGINT, signal_handler)

# Construct the correct image path
script_dir = os.path.dirname(os.path.abspath(__file__))

image_path = os.path.join(script_dir, "90-Wildlife-1200x834.jpg")  # Adjust path as needed

print("Using image path:", image_path)
add_border_and_show(image_path)
