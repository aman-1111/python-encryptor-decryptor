import tkinter as tk
from vault_ui import VaultApp

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("500x300")
    app = VaultApp(root)
    root.mainloop()
