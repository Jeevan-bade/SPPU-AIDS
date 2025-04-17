import random
import sympy  # For prime number utilities

def generate_prime_and_generator(bit_length=128):
    """
    Generate a safe prime p and a generator g for the multiplicative group
    A safe prime is p = 2q + 1 where q is also prime
    """
    while True:
        q = sympy.randprime(2**(bit_length-1), 2**bit_length - 1)
        p = 2 * q + 1
        if sympy.isprime(p):
            break
    
    # Find a generator g (primitive root modulo p)
    # For safe primes, we can test 2 and quadratic non-residues
    for g in [2, 3, 5, 6, 7, 11]:
        if pow(g, q, p) != 1 and pow(g, 2, p) != 1:
            return p, g
    
    # If none of the small values work, search for a generator
    def is_generator(g, p):
        factors = sympy.primefactors(p-1)
        return all(pow(g, (p-1)//f, p) != 1 for f in factors)
    
    for _ in range(100):
        g = random.randint(2, p-2)
        if is_generator(g, p):
            return p, g
    
    raise ValueError("Failed to find generator")

def generate_private_key(p):
    """Generate a random private key (1 < a < p-1)"""
    return random.randint(2, p-2)

def generate_public_key(g, a, p):
    """Generate public key A = g^a mod p"""
    return pow(g, a, p)

def generate_shared_secret(B, a, p):
    """Generate shared secret s = B^a mod p"""
    return pow(B, a, p)

def main():
    # Step 1: Generate public parameters (normally done once and reused)
    print("Generating public parameters (p and g)...")
    p, g = generate_prime_and_generator(64)  # Using 64-bit for demonstration
    print(f"Prime modulus (p): {p}")
    print(f"Generator (g): {g}\n")

    # A's side
    a = generate_private_key(p)
    A = generate_public_key(g, a, p)
    print(f"A's private key (a): {a}")
    print(f"A's public key (A): {A}\n")

    # B's side
    b = generate_private_key(p)
    B = generate_public_key(g, b, p)
    print(f"B's private key (b): {b}")
    print(f"B's public key (B): {B}\n")

    # Shared secret computation
    A_shared_secret = generate_shared_secret(B, a, p)
    B_shared_secret = generate_shared_secret(A, b, p)

    print(f"A's shared secret: {A_shared_secret}")
    print(f"B's shared secret: {B_shared_secret}")
    print("Success:", A_shared_secret == B_shared_secret)

if __name__ == "__main__":
    main()