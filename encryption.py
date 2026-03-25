import os
from cryptography.hazmat.primitives.kdf.scrypt import Scrypt
from cryptography.hazmat.primitives.ciphers.aead import AESGCM


SALT_SIZE = 16
NONCE_SIZE = 12
KEY_SIZE = 32  # AES-256


# =========================
# KEY DERIVATION
# =========================
def derive_key(password: str, salt: bytes) -> bytes:
    kdf = Scrypt(
        salt=salt,
        length=KEY_SIZE,
        n=2**15,
        r=8,
        p=1,
    )
    return kdf.derive(password.encode())


# =========================
# ENCRYPT
# =========================
def encrypt(data: bytes, password: str) -> bytes:
    salt = os.urandom(SALT_SIZE)
    key = derive_key(password, salt)

    aesgcm = AESGCM(key)
    nonce = os.urandom(NONCE_SIZE)

    ciphertext = aesgcm.encrypt(nonce, data, None)

    return salt + nonce + ciphertext


# =========================
# DECRYPT
# =========================
def decrypt(token: bytes, password: str) -> bytes:
    salt = token[:SALT_SIZE]
    nonce = token[SALT_SIZE:SALT_SIZE + NONCE_SIZE]
    ciphertext = token[SALT_SIZE + NONCE_SIZE:]

    key = derive_key(password, salt)
    aesgcm = AESGCM(key)

    return aesgcm.decrypt(nonce, ciphertext, None)


# =========================
# CLI EXAMPLE USAGE
# =========================
if __name__ == "__main__":
    password = input("Enter password: ").strip()
    message = input("Enter message: ").encode()

    encrypted = encrypt(message, password)
    print("\nEncrypted (bytes):", encrypted)

    decrypted = decrypt(encrypted, password)
    print("Decrypted:", decrypted.decode())
