# Image Encryption and Decryption using Pixel Manipulation

## Description
This Python script enables the encryption and decryption of images using pixel manipulation techniques. It provides options to encrypt an image, decrypt an encrypted image, and display the paths and images.

## Requirements
- Python 3.x
- OpenCV (cv2) library

## Installing OpenCV

Before running the script, you need to install the OpenCV library. You can install it via pip using the following command:

```bash
pip install opencv-python-headless
```
## Usage
1. Run the script in a Python environment with the necessary dependencies installed.
2. Follow the on-screen instructions to choose between encrypting an image, decrypting an encrypted image, or exiting the program.
3. Provide the path to the image file you want to encrypt or decrypt when prompted.
4. For encryption, specify the output path for the encrypted image.
5. For decryption, specify the output path for the decrypted image.

## Script Files
- **image_encrypt_decrypt.py**: The main script file containing functions for image encryption, decryption, and user interaction.
- **encrypted_image.png**: The output file generated after encryption. (Will be overwritten each time the script encrypts an image.)
- **decrypted_image.png**: The output file generated after decryption. (Will be overwritten each time the script decrypts an image.)

## Functions
- `encrypt_image(image_path, key, output_path)`: Encrypts the image located at image_path using the provided key and saves the result to output_path.
- `decrypt_image(image_path, key, output_path)`: Decrypts the encrypted image located at image_path using the provided key and saves the result to output_path.
- `get_full_image_path(image_path)`: Returns the absolute path of the given image file.
- `check_image_exists(image_path)`: Checks if the image file exists at the specified path.
- `load_and_display_image(image_path)`: Loads and displays the image located at image_path.


## Note
- Ensure that the image file paths provided are valid.
- The key used for encryption and decryption should be kept confidential.
- This script is for educational purposes and should not be used for sensitive data without proper encryption measures.
