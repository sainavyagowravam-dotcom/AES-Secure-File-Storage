from cryptography.fernet import Fernet
import hashlib
import json
import os
from datetime import datetime

# Step 1: Generate AES Key
key = Fernet.generate_key()
cipher = Fernet(key)

# Save key securely
with open("secret.key", "wb") as key_file:
    key_file.write(key)

# Step 2: Choose file to encrypt
file_path = input("Enter file path to encrypt: ")

with open(file_path, "rb") as file:
    data = file.read()

# Step 3: Encrypt file
encrypted_data = cipher.encrypt(data)

encrypted_file = file_path + ".enc"
with open(encrypted_file, "wb") as file:
    file.write(encrypted_data)

# Step 4: Hash for integrity check
file_hash = hashlib.sha256(data).hexdigest()

# Step 5: Store metadata
metadata = {
    "original_file": os.path.basename(file_path),
    "encrypted_file": os.path.basename(encrypted_file),
    "timestamp": str(datetime.now()),
    "hash": file_hash
}

with open("metadata.json", "w") as meta:
    json.dump(metadata, meta, indent=4)

print("\nFile encrypted successfully!")
print("Encrypted file:", encrypted_file)
print("Key saved as secret.key")