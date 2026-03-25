from cryptography.fernet import Fernet
import hashlib
import json

# Load AES key
with open("secret.key", "rb") as key_file:
    key = key_file.read()

cipher = Fernet(key)

# Load metadata
with open("metadata.json", "r") as meta:
    metadata = json.load(meta)

encrypted_file = metadata["encrypted_file"]

# Read encrypted file
with open(encrypted_file, "rb") as file:
    encrypted_data = file.read()

# Decrypt file
decrypted_data = cipher.decrypt(encrypted_data)

# Verify integrity
calculated_hash = hashlib.sha256(decrypted_data).hexdigest()

if calculated_hash == metadata["hash"]:
    output_file = "decrypted_" + metadata["original_file"]
    with open(output_file, "wb") as file:
        file.write(decrypted_data)

    print("\nFile decrypted successfully!")
    print("Integrity verified ✔")
else:
    print("\nFile integrity check failed ❌")