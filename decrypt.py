from cryptography.fernet import Fernet
# Load the decryption key
with open("/path-to-decryption-key/", "rb") as key_file:
    decryption_key = key_file.read()

# Load the encrypted file
with open("/path-to-encypted-file/", "rb") as encrypted_file:
    encrypted_data = encrypted_file.read()

# Decrypt the data
fernet = Fernet(decryption_key)
decrypted_data = fernet.decrypt(encrypted_data)

# Write the decrypted data to a new file
with open("/path-to-new-decrypted-file/", "wb") as decrypted_file:
    decrypted_file.write(decrypted_data)

print("File decrypted successfully.")
