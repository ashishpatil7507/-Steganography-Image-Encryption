# 🔐 Image Steganography - Encryption & Decryption Guide Bu ashish ramling patil
from cryptography.fernet import Fernet
import cv2
import numpy as np
import os

# Function to generate and save a key
def generate_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)
    print("\n🔑 Key generated and saved as 'key.key'. Keep it safe!\n")
    return key

# Function to encrypt a message
def encrypt_message(message, key):
    cipher = Fernet(key)
    return cipher.encrypt(message.encode()).decode()

# Function to hide encrypted text inside an image using LSB steganography
def hide_text_in_image(image_path, text, output_path):
    img = cv2.imread(image_path, cv2.IMREAD_COLOR)  # Ensure RGB mode

    if img is None:
        raise FileNotFoundError(f"🚫 Image '{image_path}' not found!")

    height, width, channels = img.shape
    total_pixels = height * width * channels
    flat_img = img.reshape(-1).astype(np.uint8)

    # Convert text to binary
    binary_text = ''.join(format(ord(char), '08b') for char in text) + '1111111111111110'  # End delimiter

    if len(binary_text) > total_pixels:
        raise ValueError("❌ Text is too long to hide in this image!")

    # Hide text in the image safely
    for i in range(len(binary_text)):
        new_value = (flat_img[i] & 0b11111110) | int(binary_text[i])  # Use bitwise operations safely
        flat_img[i] = np.uint8(new_value)  # Ensure within uint8 range

    img_stego = flat_img.reshape(img.shape)
    cv2.imwrite(output_path, img_stego)
    print(f"\n✅ Encrypted message hidden in '{output_path}'.\n")

# Main function
def main():
    print("\n🔐 IMAGE STEGANOGRAPHY - ENCRYPTION 🔐\n")
    image_path = input("🖼️ Enter the path of the image: ").strip('"')
    secret_text = input("✍️ Enter the secret text to hide: ")

    # Generate and save the encryption key
    key = generate_key()

    encrypted_message = encrypt_message(secret_text, key)

    output_image = "stego_image.png"
    hide_text_in_image(image_path, encrypted_message, output_image)

if __name__ == "__main__":
    main()
