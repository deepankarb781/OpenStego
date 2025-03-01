import cv2
import os
import string

def encrypt_message(200.JPG, message, password, output_path="encryptedImage.jpg"):
    img = cv2.imread(200.JPG)  # Load image

    if img is None:
        print("Error: Unable to load image. Check the path.")
        return

    d = {chr(i): i for i in range(255)}  # Create ASCII dictionary

    n, m, z = 0, 0, 0  # Coordinates for pixel modification

    for char in message:
        img[n, m, z] = d[char]  # Store ASCII value in pixels
        n += 1
        m += 1
        z = (z + 1) % 3  # Cycle through R, G, B channels

    cv2.imwrite(output_path, img)  # Save encrypted image
    os.system(f"start {output_path}")  # Open image (Windows)

    print("Encryption successful! Encrypted image saved as:", output_path)

if __name__ == "__main__":
    img_path = input("Enter image path: ")
    msg = input("Enter secret message: ")
    passcode = input("Enter a passcode: ")
    encrypt_message(img_path, msg, passcode)
