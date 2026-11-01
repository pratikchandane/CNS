
import hashlib

# Step 1: Accept input from user
text = input("Enter the text: ")

# Step 2: Convert text into bytes
text_bytes = text.encode()

# Step 3: Calculate SHA-1 hash
sha1_hash = hashlib.sha1(text_bytes).hexdigest()

# Step 4: Display original text and hash
print("\nOriginal Text:", text)
print("SHA-1 Digest:", sha1_hash)

# Step 5: Modify the input text
modified_text = text + "1"

# Step 6: Calculate hash of modified text
modified_bytes = modified_text.encode()
modified_hash = hashlib.sha1(modified_bytes).hexdigest()

# Step 7: Display modified text and hash
print("\nModified Text:", modified_text)
print("Modified SHA-1 Digest:", modified_hash)

# Step 8: Compare both hashes
if sha1_hash == modified_hash:
    print("\nBoth Digests are Same")
else:
    print("\nBoth Digests are Different")
    print("Avalanche Effect Demonstrated!")
