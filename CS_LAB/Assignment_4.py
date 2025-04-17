import random

def is_prime(n):
    """Check if a number is prime"""
    if n < 2:
        return False
    for p in [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]:
        if n % p == 0:
            return n == p
    d = n - 1
    s = 0
    while d % 2 == 0:
        d //= 2
        s += 1
    for a in [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]:
        if a >= n:
            continue
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(s - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True

def generate_prime(bits):
    """Generate a random prime number with specified bits"""
    while True:
        p = random.getrandbits(bits)
        # Ensure it's odd and has the right number of bits
        p |= (1 << bits - 1) | 1
        if is_prime(p):
            return p

def gcd(a, b):
    """Compute the greatest common divisor"""
    while b != 0:
        a, b = b, a % b
    return a

def multiplicative_inverse(e, phi):
    """Find the multiplicative inverse of e modulo phi"""
    d = 0
    x1, x2 = 0, 1
    y1, y2 = 1, 0
    temp_phi = phi
    
    while e > 0:
        temp1 = temp_phi // e
        temp2 = temp_phi - temp1 * e
        temp_phi = e
        e = temp2
        
        x = x2 - temp1 * x1
        y = y2 - temp1 * y1
        
        x2 = x1
        x1 = x
        y2 = y1
        y1 = y
    
    if temp_phi == 1:
        return y2 % phi

def generate_keypair(bits=8):
    """Generate public and private key pair"""
    # Choose two distinct prime numbers
    p = generate_prime(bits)
    q = generate_prime(bits)
    while q == p:
        q = generate_prime(bits)
    
    # Compute n = p * q
    n = p * q
    
    # Compute Euler's totient function
    phi = (p - 1) * (q - 1)
    
    # Choose e such that 1 < e < phi and gcd(e, phi) = 1
    e = random.randrange(1, phi)
    while gcd(e, phi) != 1:
        e = random.randrange(1, phi)
    
    # Compute d, the modular multiplicative inverse of e
    d = multiplicative_inverse(e, phi)
    
    # Public key is (e, n), private key is (d, n)
    return ((e, n), (d, n))

def encrypt_number(public_key, number):
    """Encrypt a number using the public key"""
    e, n = public_key
    # The number must be less than n
    if number >= n:
        raise ValueError("Number must be less than n for RSA encryption")
    return pow(number, e, n)

def decrypt_number(private_key, encrypted_number):
    """Decrypt a number using the private key"""
    d, n = private_key
    return pow(encrypted_number, d, n)

# Demonstration
if __name__ == '__main__':
    print("Generating RSA key pair...")
    public, private = generate_keypair(8)  # Using 8-bit primes for demonstration
    
    print(f"Public key (e, n): {public}")
    print(f"Private key (d, n): {private}")
    
    try:
        # Get numeric input from user
        number = int(input("\nEnter a number to encrypt: "))
        
        encrypted = encrypt_number(public, number)
        print(f"Encrypted number: {encrypted}")
        
        decrypted = decrypt_number(private, encrypted)
        print(f"Decrypted number: {decrypted}")
        
        if number == decrypted:
            print("Success! The decrypted number matches the original.")
        else:
            print("Error: Decryption failed!")
            
    except ValueError as e:
        print(f"Error: {e}")