import cv2
import os
import sys


def encrypt_image(image_path, key, output_path):
    # Check if the input image exists
    if not os.path.isfile(image_path):
        raise FileNotFoundError(f"Input image file '{image_path}' not found.")

    image = cv2.imread(image_path)

    # Check if the image was loaded correctly
    if image is None:
        raise ValueError(f"Unable to load image file '{image_path}'.")

    # Applying a simple mathematical operation
    encrypted_image = (image + key) % 256

    # Swapping pixels (simple example)
    encrypted_image = encrypted_image[:, ::-1]  # Reverse columns

    cv2.imwrite(output_path, encrypted_image)


def decrypt_image(image_path, key, output_path):
    # Check if the input image exists
    if not os.path.isfile(image_path):
        raise FileNotFoundError(f"Input image file '{image_path}' not found.")

    image = cv2.imread(image_path)

    # Check if the image was loaded correctly
    if image is None:
        raise ValueError(f"Unable to load image file '{image_path}'.")

    # Reverse the pixel swap
    decrypted_image = image[:, ::-1]

    # Reverse the mathematical operation
    decrypted_image = (decrypted_image - key) % 256

    cv2.imwrite(output_path, decrypted_image)


def get_full_image_path(image_path):
    return os.path.abspath(image_path)


def check_image_exists(image_path):
    if not os.path.isfile(image_path):
        raise FileNotFoundError(f"Input image file '{image_path}' not found.")


def load_and_display_image(image_path):
    image = cv2.imread(image_path)
    if image is None:
        raise ValueError(f"Unable to load image file '{image_path}'.")

    cv2.imshow('Loaded Image', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


encrypted_path = 'encrypted_image.png'
decrypted_path = 'decrypted_image.png'
key = 50
while True:
    print("Image Encryption and Decryption using Pixel Manipulation")
    print("1.Encrypte the image")
    print("2.Decrypt the encrypted image")
    print("3.exit")
    choice = int(input("enter ur choice:"))
    if choice == 1:
        image_path1 = input("Enter the path to the image file to encrypt: ")
        try:
            # Encrypt the image
            encrypt_image(image_path1, key, encrypted_path)
            print(f"Image encrypted succefully")
        except (FileNotFoundError, ValueError) as e:
            print(e)
        while True:
            print("1. View image path")
            print("2.display encrypted image")
            print("3. Exit")

            choice = input("Enter your choice (1-4): ")

            if choice == '1':
                full_image_path = get_full_image_path(encrypted_path)
                print(f"Full image path: {full_image_path}")

            elif choice == '2':
                try:
                    check_image_exists(encrypted_path)
                    load_and_display_image(encrypted_path)
                except (FileNotFoundError, ValueError) as e:
                    print(e)

            elif choice == '3':
                break

            else:
                print("Invalid choice. Please enter a number between 1 and 4.")
    elif choice == 2:
        image_path2 = input("Enter the path to the image file to decrypt:")
        try:
            # Decrypt the image
            decrypt_image(image_path2, key, decrypted_path)
            print(f"Image decrypted succefully")
        except (FileNotFoundError, ValueError) as e:
            print(e)
        while True:
            print("1. View image path")
            print("2.display decrypted image")
            print("3. Exit")

            choice = input("Enter your choice: ")

            if choice == '1':
                full_image_path = get_full_image_path(decrypted_path)
                print(f"Full image path: {full_image_path}")

            elif choice == '2':
                try:
                    check_image_exists(decrypted_path)
                    load_and_display_image(decrypted_path)
                except (FileNotFoundError, ValueError) as e:
                    print(e)

            elif choice == '3':
                break
    elif choice == 3:
        print("Exiting the program.")
        sys.exit()
    else:
        print("select correct choice")