
import os
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
from cryptography.exceptions import InvalidTag


# AES encryption function (Alice - Sender)
def encrypt_image(image_path, encrypted_path, key_path):

    # Generate a 256-bit secret key
    key = AESGCM.generate_key(bit_length=256)

    # Save the secret key separately
    with open(key_path, "wb") as key_file:
        key_file.write(key)

    # Read the original image
    with open(image_path, "rb") as image_file:
        image_data = image_file.read()

    # Create AES-GCM object
    aes = AESGCM(key)

    # Generate a random 12-byte nonce
    nonce = os.urandom(12)

    # Additional authenticated data
    aad = b"Secure Image Transfer"

    # Encrypt the image
    ciphertext = aes.encrypt(nonce, image_data, aad)

    # Store nonce + ciphertext + authentication tag
    with open(encrypted_path, "wb") as encrypted_file:
        encrypted_file.write(nonce + ciphertext)

    print("Image encrypted successfully!")
    print("Encrypted file:", encrypted_path)
    print("Secret key saved separately:", key_path)


# AES decryption function (Bob - Receiver)
def decrypt_image(encrypted_path, output_path, key_path):

    # Read the secret key
    with open(key_path, "rb") as key_file:
        key = key_file.read()

    # Read encrypted image data
    with open(encrypted_path, "rb") as encrypted_file:
        encrypted_data = encrypted_file.read()

    # Extract nonce (first 12 bytes)
    nonce = encrypted_data[:12]

    # Extract ciphertext and authentication tag
    ciphertext = encrypted_data[12:]

    # Create AES-GCM object
    aes = AESGCM(key)

    # Same additional authenticated data
    aad = b"Secure Image Transfer"

    try:
        # Decrypt and verify the image
        decrypted_data = aes.decrypt(nonce, ciphertext, aad)

        # Save the original image
        with open(output_path, "wb") as output_file:
            output_file.write(decrypted_data)

        print("Image decrypted successfully!")
        print("Recovered image:", output_path)
        print("Integrity verified successfully!")

    except InvalidTag:
        print("ERROR: Image was modified or key is incorrect!")
        print("Integrity verification failed!")


# Main program
print("===== SECURE IMAGE TRANSFER SYSTEM =====")
print("1. Encrypt Image (Alice)")
print("2. Decrypt Image (Bob)")

choice = input("Enter your choice (1 or 2): ")

if choice == "1":

    image_path = input("Enter original image path: ")
    encrypted_path = input("Enter encrypted file name: ")
    key_path = input("Enter secret key file name: ")

    encrypt_image(image_path, encrypted_path, key_path)

elif choice == "2":

    encrypted_path = input("Enter encrypted file path: ")
    output_path = input("Enter output image name: ")
    key_path = input("Enter secret key file path: ")

    decrypt_image(encrypted_path, output_path, key_path)

else:
    print("Invalid choice!")
