# 🔐 SecureStego – Image-Based Text Encryption using Steganography

**Developed by:** *Ashish Patil *  
**Language:** Python 3.x  
**Libraries Used:** `cryptography`, `pillow`, `numpy`, `opencv-python`

---

## 🧩 Overview

**SecureStego** is a Python-based project that combines **AES-128 encryption (Fernet)** and **LSB image steganography** to hide secret text inside images.  
It ensures both **data confidentiality** and **information concealment** by encrypting the message and embedding it invisibly into an image.

The encryption key is **automatically generated** and saved as `key.key`, which is required to decrypt the hidden message later.

---

## 🔑 Key Features

- 🧠 **Dual Layer Security** – Combines encryption and steganography for high data protection.  
- 🔒 **AES-128 Encryption (Fernet)** – Uses Fernet’s symmetric encryption with CBC mode and HMAC.  
- 🗝️ **Automatic Key Generation** – A 32-byte (256-bit) key is securely generated and stored in `key.key`.  
- 🖼️ **Image-Based Data Hiding** – Encrypts and embeds secret text inside an image using **LSB manipulation**.  
- 🔓 **Key-Based Decryption** – The same key is mandatory to recover the hidden message.  
- ⚙️ **User-Friendly CLI Interface** – Simple command-line input/output system.  
- 🧰 **Cross-Platform Support** – Works seamlessly on Windows, macOS, and Linux.

---

## ⚙️ Installation

Before running the project, install all required libraries:

```bash
- pip install cryptography pillow numpy opencv-python 
```


## 🚀 Usage Guide
🧩 Step 1: Encryption (Hide Secret Text)

Run the encryption script:

python encryption.py

## Input Prompts:

- Enter the path of the source image (e.g., input.png)

- Enter the secret message to hide

## Output:

- A stego image named stego_image.png with the hidden encrypted text

- A key file key.key for future decryption

## 🗝️ Important: Keep key.key safe — it’s required for decryption!

🔍 Step 2: Decryption (Extract Hidden Text)

Run the decryption script:

- python decryption.py

## Input Prompts:

- Enter the path of the stego image (e.g., stego_image.png)

- Enter the path of the key file (e.g., key.key)

## Output:

- Displays the decrypted hidden message

## 🧠 Working Principle

## Encryption:
- The input text is encrypted using Fernet (AES-128) with an auto-generated key.

## Embedding:
- The encrypted data is converted to binary and hidden in the Least Significant Bits (LSB) of image pixels.

Extraction:
- The binary data is retrieved from the stego image and reconstructed into ciphertext.

Decryption:
- The ciphertext is decrypted using the saved key to reveal the original message.
