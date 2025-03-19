from cryptography.fernet import Fernet
import cv2
import numpy as np

def load_key(key_path):
    with open(key_path, "rb") as key_file:
        return key_file.read()

def extract_text_from_image(image_path):
    img = cv2.imread(image_path)
    flat_img = img.flatten()
    
    binary_text = ""
    for i in range(len(flat_img)):
        binary_text += str(flat_img[i] & 1)
    
    chars = [binary_text[i:i+8] for i in range(0, len(binary_text), 8)]
    extracted_text = "".join([chr(int(char, 2)) for char in chars if int(char, 2) != 0])
    
    return extracted_text

def decrypt_message(encrypted_message, key):
    cipher = Fernet(key)
    return cipher.decrypt(encrypted_message.encode()).decode()

def main():
    print("\n🔓 IMAGE STEGANOGRAPHY - DECRYPTION 🔓\n")
    
    image_path = input("🖼️ Enter the path of the stego image: ")
    key_path = input("🔑 Enter the path of the key file: ")
    
    try:
        key = load_key(key_path)
        encrypted_text = extract_text_from_image(image_path)
        decrypted_message = decrypt_message(encrypted_text, key)
        print(f"\n✅ Decrypted Message: {decrypted_message}")
    except Exception as e:
        print("\n❌ Decryption failed! Ensure you're using the correct key.")
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
