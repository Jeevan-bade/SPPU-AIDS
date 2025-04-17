from ecdsa import SECP256k1
import os   

# Step 1: Access the curve and the generator point
curve = SECP256k1.curve  # No need to call it as a function
order = SECP256k1.order
G = SECP256k1.generator

# Step 2: Generate a private key (random integer between 1 and order-1)
private_key = int.from_bytes(os.urandom(32), "big") % (order - 1)

# Step 3: Calculate the public key (Q = dP)
public_key = private_key * G

# Step 4: Display Private Key and Public Key
print("Private Key:", private_key)
print("Public Key (Q):", public_key)