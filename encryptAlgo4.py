
# Custom Encryption and Decryption using XOR

def encrypt(plaintext, key):

    encrypted = ""

    for i in range(len(plaintext)):

        # Get ASCII value of plaintext character
        p = ord(plaintext[i])

        # Get ASCII value of key character
        k = ord(key[i % len(key)])

        # Perform XOR operation
        encrypted_value = p ^ k

        # Convert encrypted value into hexadecimal
        encrypted += format(encrypted_value, '02x')

    return encrypted


def decrypt(ciphertext, key):

    decrypted = ""

    # Convert hexadecimal ciphertext into bytes
    encrypted_bytes = bytes.fromhex(ciphertext)

    for i in range(len(encrypted_bytes)):

        # Get encrypted value
        c = encrypted_bytes[i]

        # Get ASCII value of key character
        k = ord(key[i % len(key)])

        # Perform XOR operation again
        original_value = c ^ k

        # Convert ASCII value into character
        decrypted += chr(original_value)

    return decrypted


# Main Program

print("CUSTOM ENCRYPTION AND DECRYPTION")

plaintext = input("Enter message: ")
key = input("Enter secret key: ")

if key == "":
    print("Error: Key cannot be empty!")

else:
    # Encryption
    ciphertext = encrypt(plaintext, key)

    print("\nEncrypted Message:", ciphertext)

    # Decryption
    original_message = decrypt(ciphertext, key)

    print("Decrypted Message:", original_message)

    if original_message == plaintext:
        print("Encryption and Decryption Successful!")
