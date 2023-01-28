import os
import unittest
from tienc import RSAEncryption, AESEncryption, HybridEncryption


class TestEncryptionMethods(unittest.TestCase):

    def test_rsa_encryption(self):
        encryption = RSAEncryption()
        message = "This is a test message"
        message = message.encode()
        ciphertext = encryption.encrypt(message)
        plaintext = encryption.decrypt(ciphertext)
        self.assertEqual(message, plaintext.encode())

    def test_aes_encryption(self):
        encryption = AESEncryption()
        message = "This is a test message"
        message = message.encode()
        ciphertext = encryption.encrypt(message)
        plaintext = encryption.decrypt(ciphertext)
        self.assertEqual(message, plaintext.encode())

    def test_hybrid_encryption(self):
        encryption = HybridEncryption()

        text = "This is a test message"
        text = text.encode()
        aes_ciphertext, encrypted_key = encryption.encrypt_text(text)
        decrypted_text = encryption.decrypt_text(aes_ciphertext, encrypted_key)
        self.assertEqual(text, decrypted_text.encode())

        image_path = "test_image.jpg"
        with open(image_path, 'wb') as image_file:
            image_file.write(b"Test image data")
        aes_ciphertext, encrypted_key = encryption.encrypt_image(image_path)
        decryption_image_path = "decryption_image.jpg"
        encryption.decrypt_image(aes_ciphertext, encrypted_key, decryption_image_path)
        self.assertEqual(os.path.getsize(image_path), os.path.getsize(decryption_image_path))
        with open(image_path, 'rb') as original_image_file, open(decryption_image_path, 'rb') as decryption_image_file:
            self.assertEqual(original_image_file.read(), decryption_image_file.read())

        os.remove(image_path)
        os.remove(decryption_image_path)


if __name__ == '__main__':
    unittest.main()
