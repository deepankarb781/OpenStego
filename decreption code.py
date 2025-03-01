import cv2

def decrypt_message(image_path, original_message_length, correct_password):
    img = cv2.imread(image_path)  # Load encrypted image

    if img is None:
        print("Error: Unable to load image. Check the path.")
        return

    c = {i: chr(i) for i in range(255)}  # Reverse ASCII dictionary

    n, m, z = 0, 0, 0  # Coordinates for pixel reading
    decrypted_message = ""

    user_password = input("Enter passcode for decryption: ")

    if user_password == correct_password:
        for _ in range(original_message_length):
            decrypted_message += c[img[n, m, z]]
            n += 1
            m += 1
            z = (z + 1) % 3  # Cycle through R, G, B channels

        print("Decryption successful! Message:", decrypted_message)
    else:
        print("ERROR: Unauthorized access! Wrong passcode.")

if __name__ == "__main__":
    img_path = input("Enter encrypted image path: ")
    msg_length = int(input("Enter original message length: "))  # Needed to correctly extract the message
    passcode = input("Enter the original passcode used for encryption: ")
    decrypt_message(img_path, msg_length, passcode)
