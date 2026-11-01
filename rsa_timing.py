
import time
import os
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes

# RSA key sizes
key_sizes = [1024, 2048, 3072, 4096]

# Message sizes in bits
message_sizes = [64, 128, 256]

# Number of repetitions for timing
REPEAT = 100

print("RSA PERFORMANCE ANALYSIS")
print("-" * 75)

for key_size in key_sizes:

    print("\nRSA Key Size:", key_size, "bits")

    # 1. Key Pair Generation
    start = time.perf_counter()

    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=key_size
    )

    public_key = private_key.public_key()

    key_time = time.perf_counter() - start

    print("Key Generation Time:", round(key_time, 6), "seconds")

    # Test different message sizes
    for msg_size in message_sizes:

        # Generate message of required bit length
        message = os.urandom(msg_size // 8)
        message = bytes([message[0] | 128]) + message[1:]

        # 2. Encryption
        start = time.perf_counter()

        for i in range(REPEAT):
            ciphertext = public_key.encrypt(
                message,
                padding.OAEP(
                    mgf=padding.MGF1(
                        algorithm=hashes.SHA256()
                    ),
                    algorithm=hashes.SHA256(),
                    label=None
                )
            )

        encryption_time = (
            time.perf_counter() - start
        ) / REPEAT

        # 3. Decryption
        start = time.perf_counter()

        for i in range(REPEAT):
            decrypted_message = private_key.decrypt(
                ciphertext,
                padding.OAEP(
                    mgf=padding.MGF1(
                        algorithm=hashes.SHA256()
                    ),
                    algorithm=hashes.SHA256(),
                    label=None
                )
            )

        decryption_time = (
            time.perf_counter() - start
        ) / REPEAT

        # Verify original and decrypted messages
        if message == decrypted_message:
            result = "Successful"
        else:
            result = "Failed"

        print("\nMessage Size:", msg_size, "bits")
        print("Encryption Time:", round(encryption_time, 8), "seconds")
        print("Decryption Time:", round(decryption_time, 8), "seconds")
        print("Verification:", result)

print("\nRSA EXPERIMENT COMPLETED")
