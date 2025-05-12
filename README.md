# Python Encryptor-Decrypter 🔐

A simple Python-based command-line tool to encrypt and decrypt text using basic cryptographic techniques. This project is ideal for learning and experimenting with text-based encryption.

## Features

- Encrypt plain text into a secure format
- Decrypt encrypted text back to original
- Easy to use via command line
- Fully written in Python
- Extendable for stronger algorithms

## Demo

```bash
$ python encryptor.py -e "Hello, World!"
Encrypted Text: Khoor, Zruog!

$ python encryptor.py -d "Khoor, Zruog!"
Decrypted Text: Hello, World!

    Example above is based on Caesar cipher with a shift of 3.

Requirements

    Python 3.x

No external libraries required.
Installation

    Clone the repository:

git clone https://github.com/your-username/python-encryptor-decryptor.git
cd python-encryptor-decryptor

    Run the script:

python encryptor.py

Usage

Use the script via command line with the following options:

python encryptor.py -e "your text here"    # Encrypt text
python encryptor.py -d "your text here"    # Decrypt text

Options
Option	Description
-e	Encrypt text
-d	Decrypt text
File Structure

python-encryptor-decryptor/
├── encryptor.py     # Main script
├── README.md        # Project documentation

Customization

You can modify encryptor.py to:

    Change the encryption algorithm

    Adjust shift values (if using Caesar cipher)

    Add support for file encryption

License

This project is licensed under the MIT License.

Author: Aman Chaurasia
GitHub: @aman-1111
