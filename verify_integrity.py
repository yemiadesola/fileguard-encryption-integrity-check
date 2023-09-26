import hashlib
import os
import sys

# Calculate the hash value of a file
def calculate_hash(filename):
    sha256 = hashlib.sha256()
    with open(filename, "rb") as f:
        while True:
            data = f.read(65536)  # Read in 64k chunks
            if not data:
                break
            sha256.update(data)
    return sha256.hexdigest()

# Check if directory path or file paths are provided as arguments
if len(sys.argv) != 2 and len(sys.argv) != 3:
    print("Usage: python verify_integrity.py <directory_path | original_file decrypted_file>")
    sys.exit(1)

if len(sys.argv) == 2:
    # Directory path provided
    directory = sys.argv[1]
    original_file = os.path.join(directory, "textme.txt")
    decrypted_file = os.path.join(directory, "textme.encrypted")
else:
    # Individual file paths provided
    original_file = sys.argv[1]
    decrypted_file = sys.argv[2]

# Load the original hash saved during encryption
with open("/home/kali/Documents/encypt-decrypt/encryption-key/original_file_hash.txt", "r") as hash_file:
    original_hash = hash_file.read()

# Calculate the hash of the decrypted file
decrypted_hash = calculate_hash(decrypted_file)

# Compare the two hash values
if original_hash == decrypted_hash:
    print(f"File integrity verified. Hashes match:\nOriginal File Hash:   {original_hash}\nDecrypted File Hash: {decrypted_hash}")
else:
    print(f"File integrity check failed. Hashes do not match:\nOriginal File Hash:   {original_hash}\nDecrypted File Hash: {decrypted_hash}")
