# 🔐 Strong Python Encryption (AES-256-GCM + Scrypt)

A simple, secure Python encryption module for protecting data using modern cryptography standards.

This project provides strong symmetric encryption using:
- AES-256-GCM (encryption + integrity)
- Scrypt (secure password-based key derivation)
- Random salt and nonce per encryption

---

## ⚡ Features

- 🔐 AES-256-GCM authenticated encryption
- 🧠 Scrypt key derivation (resistant to brute-force attacks)
- 🎲 Unique salt per encryption
- 🎲 Unique nonce per message
- 📦 Simple import-and-use design
- ⚡ Lightweight (only dependency is cryptography)

---

## 📦 Installation

pip install cryptography

---

## 🚀 Usage

Import functions:
from encryption import encrypt, decrypt

Encrypt data:
data = b"Secret message"
password = "strong_password_123"

encrypted = encrypt(data, password)
print(encrypted)

Decrypt data:
decrypted = decrypt(encrypted, password)
print(decrypted.decode())

---

## 🧠 How it works

Encryption process:
- Generate random salt
- Derive encryption key using Scrypt + password
- Generate random nonce
- Encrypt using AES-256-GCM
- Output = salt + nonce + ciphertext

Decryption process:
- Extract salt + nonce
- Rebuild key using password
- Decrypt ciphertext
- Return original data

---

## 🔐 Security Model

Component | Purpose
AES-256-GCM | Secure encryption + tamper detection
Scrypt | Protects against brute-force attacks
Salt | Prevents precomputed attacks
Nonce | Ensures unique encryption each time

---

## ⚠️ Security Notes

DO NOT:
- Reuse passwords across systems
- Store passwords in code
- Modify encrypted data manually
- Reuse salt or nonce

DO:
- Use long random passwords (16+ chars recommended)
- Store keys securely (password manager recommended)
- Encrypt fresh data each time

---

## 📌 Use Cases

- Secure notes
- File encryption systems
- API data protection
- Local sensitive data storage
- Python application security

---

## 🧪 Example Output

Encrypted: b'\x9a\x02\xff...'
Decrypted: Secret message

---

## 📜 License

MIT License — free to use and modify.

---

## ⭐ Support

If you like this project:
- Star the repo
- Fork it
- Improve it
