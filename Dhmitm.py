
# Diffie-Hellman Key Exchange with MITM Attack

# Public values
p = 23
g = 5

print("Public Values:")
print("Prime number (p):", p)
print("Generator (g):", g)


# --------------------------------
# PART 1: NORMAL DIFFIE-HELLMAN
# --------------------------------

print("\n--- NORMAL DIFFIE-HELLMAN ---")

# Private keys
pratik_private = 6
prashant_private = 15

# Generate public keys
pratik_public = pow(g, pratik_private, p)
prashant_public = pow(g, prashant_private, p)

print("Pratik Public Key:", pratik_public)
print("Prashant Public Key:", prashant_public)

# Generate shared secret keys
pratik_secret = pow(prashant_public, pratik_private, p)
prashant_secret = pow(pratik_public, prashant_private, p)

print("Pratik Shared Secret:", pratik_secret)
print("Prashant Shared Secret:", prashant_secret)

if pratik_secret == prashant_secret:
    print("Normal DH: Shared keys match!")
else:
    print("Key exchange failed!")


# --------------------------------
# PART 2: MITM ATTACK
# --------------------------------

print("\n--- MAN-IN-THE-MIDDLE ATTACK ---")

# Eve's two private keys
eve_private_for_pratik = 9
eve_private_for_prashant = 7

# Eve generates two public keys
eve_public_for_pratik = pow(g, eve_private_for_pratik, p)
eve_public_for_prashant = pow(g, eve_private_for_prashant, p)

# Eve intercepts Pratik's public key
# and sends her own public key to Prashant
print("\nEve intercepts Pratik's public key:", pratik_public)
print("Eve sends her public key to Prashant:", eve_public_for_prashant)

# Eve intercepts Prashant's public key
# and sends her own public key to Pratik
print("\nEve intercepts Prashant's public key:", prashant_public)
print("Eve sends her public key to Pratik:", eve_public_for_pratik)

# Pratik calculates secret with Eve
pratik_mitm_secret = pow(eve_public_for_pratik,
                        pratik_private, p)

# Prashant calculates secret with Eve
prashant_mitm_secret = pow(eve_public_for_prashant,
                      prashant_private, p)

# Eve calculates the same two shared secrets
eve_pratik_secret = pow(pratik_public,
                       eve_private_for_pratik, p)

eve_prashant_secret = pow(prashant_public,
                     eve_private_for_prashant, p)

print("\nPratik's Secret Key:", pratik_mitm_secret)
print("Eve's Key with Pratik:", eve_pratik_secret)

print("Prashant's Secret Key:", prashant_mitm_secret)
print("Eve's Key with Prashant:", eve_prashant_secret)

if pratik_mitm_secret == eve_pratik_secret:
    print("\nEve successfully shares a key with Pratik!")

if prashant_mitm_secret == eve_prashant_secret:
    print("Eve successfully shares a key with Prashant!")

print("\nMITM ATTACK SUCCESSFUL!")
print("Eve can intercept and read messages.")
