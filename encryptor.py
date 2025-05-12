from cryptography.fernet import Fernet

class Encryptor:
    def __init__(self, key=None):
        self.key = key or Fernet.generate_key()
        self.fernet = Fernet(self.key)

    def encrypt_file(self, filepath):
        with open(filepath, 'rb') as file:
            data = file.read()
        encrypted = self.fernet.encrypt(data)
        with open(filepath + '.enc', 'wb') as file:
            file.write(encrypted)

    def decrypt_file(self, filepath):
        with open(filepath, 'rb') as file:
            data = file.read()
        decrypted = self.fernet.decrypt(data)
        if filepath.endswith('.enc'):
            original_path = filepath.replace('.enc', '')
            with open(original_path, 'wb') as file:
                file.write(decrypted)
            return original_path
        return None

    def get_key(self):
        return self.key.decode()
