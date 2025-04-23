import random
import string
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes


# Generate a secure password
def generate_password(length=12):
    if length < 4:
        raise ValueError("Password length should be at least 4")

    # Password needs to be strong so ensure required characters are included
    special = random.choice("!@#$%^&*()_+-=[]{}|;:,.<>?")
    #Generate a random number
    digit = random.choice(string.digits)
    #Generate uppercase and lowercase letters
    uppercase = random.choice(string.ascii_uppercase)
    lowercase = random.choice(string.ascii_lowercase)

    others = random.choices(
        string.ascii_letters + string.digits + "!@#$%^&*()_+-=[]{}|;:,.<>?",
        k=length - 3,
    )

    password_list = [special, digit, uppercase,lowercase] + others
    #move characters around to create a random string password
    random.shuffle(password_list)
    return ''.join(password_list)


# Generate RSA keys
def generate_keys():
    private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
    public_key = private_key.public_key()
    return private_key, public_key


# Use RSA to encrypt the password
def encrypt_password(password, public_key):
    encrypted = public_key.encrypt(
        password.encode(),
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None,
        ),
    )
    return encrypted


# Decrypt the password using RSA
def decrypt_password(encrypted_password, private_key):
    decrypted = private_key.decrypt(
        encrypted_password,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None,
        ),
    )
    return decrypted.decode()

# Main test
if __name__ == "__main__":
    print("Password Generator...")
    password = generate_password()
    print(f"Strong Password: {password}")

    print("\nRSA key pair Generation ...")
    #Assign both public and private key
    private_key, public_key = generate_keys()

    print("\nEncrypting password...")
    encrypted = encrypt_password(password, public_key)
    print(f"Encrypted Password (bytes): {encrypted}")

    print("\nDecrypting password...")
    decrypted = decrypt_password(encrypted, private_key)
    print(f"Decrypted Password: {decrypted}")
