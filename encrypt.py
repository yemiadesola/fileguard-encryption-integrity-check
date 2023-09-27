import sys
import hashlib
from cryptography.fernet import Fernet

# Generate an encryption key
encryption_key = Fernet.generate_key()

# Save the encryption key to a file
with open("/path/", "wb") as key_file:
    key_file.write(encryption_key)

# Provided file part as argument
if len(sys.argv) != 2:
    print("Usage: python encrypt.py <file_path>")
    sys.exit(1)
file_path = sys.argv[1]

# Read the file contents
with open(file_path, "rb") as file:
    file_data = file.read()

# Create a Fernet cipher with the encryption key
fernet = Fernet(encryption_key)

# Encrypt the file contents
encrypted_data = fernet.encrypt(file_data)

# Save the encrypted data to a file
with open("/path-to-encrypted-file/", "wb") as encrypted_file:
    encrypted_file.write(encrypted_data)

# Calculate the hash of the original file
hash_object = hashlib.sha256()
hash_object.update(file_data)
file_hash = hash_object.hexdigest()

# Save the hash to a file
with open("/path-to-hash/", "w") as hash_file:
    hash_file.write(file_hash)

print(f"File '{file_path}' encrypted successfully.")
