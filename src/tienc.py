from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.fernet import Fernet
import io


class RSAEncryption:

    """ RSA encryption class with two methods: encrypt and decrypt.
    Encrypt takes data as a parameter and returns the ciphertext.
    Decrypt takes ciphertext as a parameter and returns the decrypted data."""

    def __init__(self):
        try:
            self.private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
            self.public_key = self.private_key.public_key()
        except Exception as e:
            print("Error generating RSA key: ", e)

    def encrypt(self, data):
        try:
            ciphertext = self.public_key.encrypt(data, padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()),
                                                                    algorithm=hashes.SHA256(), label=None))
            return ciphertext
        except Exception as e:
            print("Error encrypting data with RSA: ", e)

    def decrypt(self, ciphertext):
        try:
            plaintext = self.private_key.decrypt(ciphertext, padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()),
                                                                          algorithm=hashes.SHA256(), label=None))
            return plaintext.decode()
        except Exception as e:
            print("Error decrypting data with RSA: ", e)


class AESEncryption:

    """AES encryption class with two methods: encrypt and decrypt.
    Encrypt takes data as a parameter and returns the ciphertext.
    Decrypt takes ciphertext as a parameter and returns the decrypted data."""

    def __init__(self):
        try:
            self.key = Fernet.generate_key()
            self.cipher = Fernet(self.key)
        except Exception as e:
            print("Error generating AES key: ", e)

    def encrypt(self, data):
        try:
            ciphertext = self.cipher.encrypt(data)
            return ciphertext
        except Exception as e:
            print("Error encrypting data with AES: ", e)

    def decrypt(self, ciphertext):
        try:
            plaintext = self.cipher.decrypt(ciphertext)
            return plaintext.decode()
        except Exception as e:
            print("Error decrypting data with AES: ", e)


class HybridEncryption:

    """Hybrid encryption class with four methods: encrypt_text, decrypt_text, encrypt_image, decrypt_image.
    Encrypt_text takes text as a parameter and returns the ciphertext and the encrypted key.
    Decrypt_text takes ciphertext and encrypted key as parameters and returns the decrypted text.
    Encrypt_image takes image as a parameter and returns the ciphertext and the encrypted key.
    Decrypt_image takes ciphertext and encrypted key as parameters and returns the decrypted image."""

    def __init__(self):
        self.rsa_encryption = RSAEncryption()
        self.aes_encryption = AESEncryption()

    def encrypt_text(self, text):
        try:
            aes_ciphertext = self.aes_encryption.encrypt(text)
            encrypted_key = self.rsa_encryption.encrypt(self.aes_encryption.key)
            return aes_ciphertext, encrypted_key
        except Exception as e:
            print("Error encrypting text: ", e)

    def decrypt_text(self, aes_ciphertext, encrypted_key):
        try:
            decrypted_key = self.rsa_encryption.decrypt(encrypted_key)
            aes_decryption = Fernet(decrypted_key)
            plaintext = aes_decryption.decrypt(aes_ciphertext)
            return plaintext.decode()
        except Exception as e:
            print("Error decrypting text: ", e)

    def encrypt_image(self, image_path, chunk_size=1024):
        try:
            with open(image_path, 'rb') as image_file:
                data = io.BytesIO(image_file.read())
                chunks = iter(lambda: data.read(chunk_size), b'')
                encrypted_chunks = []
                for chunk in chunks:
                    encrypted_chunk = self.aes_encryption.encrypt(chunk)
                    encrypted_chunks.append(encrypted_chunk)
            encrypted_key = self.rsa_encryption.encrypt(self.aes_encryption.key)
            return encrypted_chunks, encrypted_key
        except Exception as e:
            print("Error encrypting image: ", e)

    def decrypt_image(self, encrypted_chunks, encrypted_key, image_path):
        try:
            decrypted_key = self.rsa_encryption.decrypt(encrypted_key)
            aes_decryption = Fernet(decrypted_key)
            decrypted_data = b''.join([aes_decryption.decrypt(chunk) for chunk in encrypted_chunks])
            with open(image_path, 'wb') as image_file:
                image_file.write(decrypted_data)
        except Exception as e:
            print("Error decrypting image: ", e)
