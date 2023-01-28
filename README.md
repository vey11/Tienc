
# Tienc

Tienc is a simple library that allows you to 
encrypt and decrypt text and images Hybrid encryption, 
additionally tienc allow standalone encryption 
using either AES encryption or RSA encryption. 
Tienc is based on the ```Cryptography``` library.
Tienc contains 3 classes,
AESEncryption, RSAEncryption and HybridEncryption.

### AESEncryption

AES encryption class with two methods: ```encrypt``` and ```decrypt```.
encrypt takes data as a parameter and returns the ciphertext.
Decrypt takes ciphertext as a parameter and returns the decrypted data.

### RSAEncryption 

RSA encryption class with two methods: ```encrypt``` and ```decrypt```.
Encrypt takes data as a parameter and returns the ciphertext.
Decrypt takes ciphertext as a parameter and returns the decrypted data.

### HybridEncryption 

Hybrid encryption class with four methods: ```encrypt_text```, ```decrypt_text```, ```encrypt_image``` and ```decrypt_image```.
Encrypt_text takes text as a parameter and returns the ciphertext and the encrypted key.
Decrypt_text takes ciphertext and encrypted key as parameters and returns the decrypted text.
Encrypt_image takes image as a parameter and returns the ciphertext and the encrypted key.
Decrypt_image takes ciphertext and encrypted key as parameters and returns the decrypted image.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install Tienc.

```bash
pip install Tienc
```

## Usage

```python
hybrid_encryption = HybridEncryption()

# Encrypt text
ciphertext, encrypted_key = hybrid_encryption.encrypt_text("Hello, World!")

# Decrypt text
plaintext = hybrid_encryption.decrypt_text(ciphertext, encrypted_key)
print(plaintext) # "Hello, World!"

# Encrypt image
encrypted_chunks, encrypted_key = hybrid_encryption.encrypt_image("image.jpg")

# Decrypt image
image = hybrid_encryption.decrypt_image(encrypted_chunks, encrypted_key)
```
It's important to note that the key used in 
the ```AESEncryption``` class is generated randomly 
every time the class is instantiated, 
so the key used to encrypt the data must be 
stored in a secure location, 
if needed for future decryption.

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[MIT](https://choosealicense.com/licenses/mit/)




