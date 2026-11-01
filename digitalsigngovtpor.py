
from cryptography.hazmat.primitives.asymmetric import dsa
from cryptography.hazmat.primitives import hashes
from cryptography.exceptions import InvalidSignature

# Step 1: Generate Private Key
private_key = dsa.generate_private_key(
    key_size=2048
)

# Step 2: Generate Public Key
public_key = private_key.public_key()

print("Keys generated successfully!")

# Step 3: Enter the message
message = input("Enter the message: ")

# Convert message into bytes
message = message.encode('utf-8')

# Step 4: Create Digital Signature
signature = private_key.sign(
    message,
    hashes.SHA256()
)

print("\nDigital Signature created successfully!")
print("Signature:", signature.hex())

# Step 5: Verify Digital Signature
try:
    public_key.verify(
        signature,
        message,
        hashes.SHA256()
    )

    print("\nSignature Verified Successfully!")
    print("Message is authentic and unchanged.")

except InvalidSignature:
    print("\nSignature Verification Failed!")
    print("Message may have been modified.")

# Step 6: Test message modification
modified_message = b"Modified Tender Document"

print("\nTesting Modified Message:")

try:
    public_key.verify(
        signature,
        modified_message,
        hashes.SHA256()
    )

    print("Signature Verified Successfully!")

except InvalidSignature:
    print("Verification Failed!")
    print("Message has been modified.")
