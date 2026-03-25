 🔐 Secure File Storage System with AES-256
 
 📌 Objective
To create a secure file encryption and decryption system using AES-256 with integrity verification.

 🛠 Tools Used
- Python
- Cryptography Library (Fernet)
- CLI (Command Line Interface)

 🔒 Features
- AES-256 encryption using Fernet
- Secure file storage with `.enc` extension
- Metadata storage (filename, timestamp, hash)
- Decryption with integrity verification
- Tamper detection using SHA-256 hashing

 📁 Files
- encrypt_file.py → Encrypts file
- decrypt_file.py → Decrypts file
- metadata.json → Stores file details

▶️ How to Run

 Encrypt:
```bash
python encrypt_file.py

decrypt:
python decrypt_file.py
