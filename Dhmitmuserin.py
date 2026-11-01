
# Diffie-Hellman Key Exchange with MITM Attack

# Step 1: Take public values from user
p = int(input("Enter prime number p: "))
g = int(input("Enter generator g: "))

print("\nPublic Values:")
print("p =", p)
print("g =", g)

# Step 2: Take private keys
alice_private = int(input("Enter Alice private key: "))
bob_private = int(input("Enter Bob private key: "))

# Step 3: Generate public keys
alice_public = pow(g, alice_private, p)
bob_public = pow(g, bob_private, p)

print("\n--- NORMAL DIFFIE-HELLMAN ---")
print("Alice Public Key:", alice_public)
print("Bob Public Key:", bob_public)

# Step 4: Generate shared secret keys
alice_secret = pow(bob_public, alice_private, p)
bob_secret = pow(alice_public, bob_private, p)

print("Alice Shared Secret:", alice_secret)
print("Bob Shared Secret:", bob_secret)

if alice_secret == bob_secret:
    print("Normal DH: Shared keys match!")

# Step 5: Take Eve's private keys
eve_private_for_alice = int(input("Enter Eve private key for Alice: "))
eve_private_for_bob = int(input("Enter Eve private key for Bob: "))

# Step 6: Generate Eve's public keys
eve_public_for_alice = pow(g, eve_private_for_alice, p)
eve_public_for_bob = pow(g, eve_private_for_bob, p)

print("\n--- MITM ATTACK ---")

print("Eve intercepts Alice's key:", alice_public)
print("Eve sends her key to Bob:", eve_public_for_bob)

print("Eve intercepts Bob's key:", bob_public)
print("Eve sends her key to Alice:", eve_public_for_alice)

# Step 7: Alice and Bob calculate keys with Eve
alice_mitm_secret = pow(eve_public_for_alice,
                        alice_private, p)

bob_mitm_secret = pow(eve_public_for_bob,
                      bob_private, p)

# Step 8: Eve calculates shared keys
eve_alice_secret = pow(alice_public,
                       eve_private_for_alice, p)

eve_bob_secret = pow(bob_public,
                     eve_private_for_bob, p)

# Step 9: Display results
print("\nAlice's Secret Key:", alice_mitm_secret)
print("Eve's Key with Alice:", eve_alice_secret)

print("Bob's Secret Key:", bob_mitm_secret)
print("Eve's Key with Bob:", eve_bob_secret)

# Step 10: Verify attack
if alice_mitm_secret == eve_alice_secret:
    print("Eve successfully shares a key with Alice!")

if bob_mitm_secret == eve_bob_secret:
    print("Eve successfully shares a key with Bob!")

print("\nMITM ATTACK SUCCESSFUL!")
