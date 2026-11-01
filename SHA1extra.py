
import hashlib

# Function to generate SHA-1 hash
def generate_sha1(text):
    text_bytes = text.encode('utf-8')
    sha1_hash = hashlib.sha1(text_bytes)
    return sha1_hash.hexdigest()

# Step 1: Accept input from user
message = input("Enter the original message: ")

# Step 2: Generate SHA-1 hash
original_hash = generate_sha1(message)

# Step 3: Display original message and hash
print("\n========== ORIGINAL MESSAGE ==========")
print("Original Message:", message)
print("SHA-1 Hash:", original_hash)
print("Hash Length:", len(original_hash), "characters")

# Step 4: Modify the original message
modified_message = message + "1"

# Step 5: Generate hash of modified message
modified_hash = generate_sha1(modified_message)

# Step 6: Display modified message and hash
print("\n========== MODIFIED MESSAGE ==========")
print("Modified Message:", modified_message)
print("Modified SHA-1 Hash:", modified_hash)
print("Hash Length:", len(modified_hash), "characters")

# Step 7: Compare both hash values
print("\n========== HASH COMPARISON ==========")

if original_hash == modified_hash:
    print("Both hashes are SAME.")
else:
    print("Both hashes are DIFFERENT.")
    print("Avalanche Effect is Demonstrated!")

# Step 8: Display final result
print("\n========== RESULT ==========")
print("SHA-1 hashing performed successfully.")
print("SHA-1 produces a 160-bit (40 hexadecimal characters) digest.")
