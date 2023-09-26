# fileguard-encryption-integrity-check
FileGuard: File Encryption, Decryption, and Integrity Check

FileGuard is a Python-based utility that provides encryption, decryption, and integrity checking for files. This tool is designed to help you secure your sensitive files, ensuring that they remain confidential during storage and transfer. Additionally, it allows you to verify the integrity of your files to detect any tampering.
Features

    File Encryption: Encrypt your files using the Fernet encryption algorithm, ensuring that only authorized users can access their contents.

    File Decryption: Decrypt encrypted files to their original format, provided you have the decryption key.

    File Integrity Check: Calculate and compare hash values to verify the integrity of your files. Detect any unauthorized changes to your files.

Prerequisites
Before using FileGuard, you'll need to have Python and the following Python packages installed:

    cryptography: Used for file encryption and decryption.
    hashlib: Used for calculating hash values.

You can install these packages using pip:

bash

pip install cryptography

Usage
Encryption

To encrypt a file, use the following command:

bash
python encrypt.py <file_path>

Decryption
To decrypt an encrypted file, use the following command:

bash
python decrypt.py <encryption_key_path> <encrypted_file_path>

    <encryption_key_path>: The path to the encryption key file (usually encryption_key.txt).
    <encrypted_file_path>: The path to the encrypted file (with the .encrypted extension). The decrypted file will have the same name as the original.

Integrity Check
To verify the integrity of a file, use the following command:

bash
python verify_integrity.py <original_file_path> <decrypted_file_path>

    <original_file_path>: The path to the original (unencrypted) file.
    <decrypted_file_path>: The path to the decrypted file.

Example
Here's an example of how to use FileGuard:

    Encrypt a file:

bash

python encrypt.py my_file.txt
    Decrypt the encrypted file:

bash
python decrypt.py encryption-key/encryption_key.txt my_file.encrypted

    Verify the integrity of the decrypted file:

bash
python verify_integrity.py my_file.txt my_file.encrypted

If the integrity check is successful, you'll see a message indicating that the file integrity has been verified.
Security Considerations

    Keep the encryption key (encryption_key.txt) secure. Without it, you won't be able to decrypt your files.
    When transferring encrypted files, securely share the encryption key separately.
    Regularly check the integrity of your files to ensure they haven't been tampered with.
