import os
import tkinter as tk
from tkinter import filedialog, messagebox, simpledialog
from encryptor import Encryptor

class VaultApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Secure File Vault")
        self.encryptor = None
        self.build_ui()

    def build_ui(self):
        tk.Label(self.root, text="Secure File Vault", font=("Arial", 16)).pack(pady=10)

        tk.Button(self.root, text="Encrypt Folder", command=self.encrypt_folder, width=30).pack(pady=5)
        tk.Button(self.root, text="Decrypt Folder", command=self.decrypt_folder, width=30).pack(pady=5)
        tk.Button(self.root, text="Import Key File for Decryption", command=self.import_key, width=30).pack(pady=5)

        self.key_label = tk.Label(self.root, text="Encryption Key will appear here", wraplength=400)
        self.key_label.pack(pady=10)

    def encrypt_folder(self):
        folder_path = filedialog.askdirectory()
        if folder_path:
            self.encryptor = Encryptor()  # Generate new key
            for filename in os.listdir(folder_path):
                filepath = os.path.join(folder_path, filename)
                if os.path.isfile(filepath):
                    self.encryptor.encrypt_file(filepath)
            key = self.encryptor.get_key()
            self.key_label.config(text=f"Encryption Key:\n{key}")
            self.save_key(key)
            messagebox.showinfo("Success", "All files encrypted and key saved.")

    def save_key(self, key):
        file_path = filedialog.asksaveasfilename(defaultextension=".key", filetypes=[("Key Files", "*.key")])
        if file_path:
            with open(file_path, 'w') as f:
                f.write(key)

    def import_key(self):
        key_path = filedialog.askopenfilename(filetypes=[("Key Files", "*.key")])
        if key_path:
            with open(key_path, 'r') as f:
                key = f.read().strip()
                self.encryptor = Encryptor(key=key)
                self.key_label.config(text=f"Imported Key:\n{key}")
                messagebox.showinfo("Key Imported", "Encryption key loaded successfully.")

    def decrypt_folder(self):
        if not self.encryptor:
            key = simpledialog.askstring("Enter Key", "Please enter your encryption key:")
            if not key:
                messagebox.showerror("Missing Key", "No key provided.")
                return
            self.encryptor = Encryptor(key=key)
        folder_path = filedialog.askdirectory()
        if folder_path:
            for filename in os.listdir(folder_path):
                if filename.endswith(".enc"):
                    filepath = os.path.join(folder_path, filename)
                    try:
                        self.encryptor.decrypt_file(filepath)
                    except Exception as e:
                        print(f"Failed to decrypt {filename}: {e}")
            messagebox.showinfo("Success", "Decryption complete.")
