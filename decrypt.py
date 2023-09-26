from cryptography.fernet import Fernet

# Load the decryption key
with open("/home/kali/Documents/encypt-decrypt/encryption-key/encryption_key.txt", "rb") as key_file:
    decryption_key = key_file.read()

# Load the encrypted file
with open("/home/kali/Documents/encypt-decrypt/encryption-key/textme.encrypted", "rb") as encrypted_file:
    encrypted_data = encrypted_file.read()

# Decrypt the data
fernet = Fernet(decryption_key)
decrypted_data = fernet.decrypt(encrypted_data)

# Write the decrypted data to a new file (e.g., decrypted_textme.txt)
with open("/home/kali/Documents/encypt-decrypt/myfile/decrypted_textme.txt", "wb") as decrypted_file:
    decrypted_file.write(decrypted_data)

print("File decrypted successfully.")
