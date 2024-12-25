import tkinter as tk
from tkinter import messagebox
from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad
import base64

def encrypt(plain_text, key):
    cipher = DES.new(key, DES.MODE_CBC)
    ct_bytes = cipher.encrypt(pad(plain_text.encode(), DES.block_size))
    iv = base64.b64encode(cipher.iv).decode('utf-8')
    ct = base64.b64encode(ct_bytes).decode('utf-8')
    return iv, ct

def decrypt(cipher_text, key, iv):
    cipher = DES.new(key, DES.MODE_CBC, base64.b64decode(iv))
    pt = unpad(cipher.decrypt(base64.b64decode(cipher_text)), DES.block_size)
    return pt.decode('utf-8')

def on_encrypt():
    key = key_entry.get().encode('utf-8')
    plain_text = text_entry.get("1.0", tk.END).strip()

    if len(key) != 8:
        messagebox.showerror("Error", "Kunci harus 8 byte.")
        return

    iv, ct = encrypt(plain_text, key)
    result_text.delete("1.0", tk.END)
    result_text.insert(tk.END, f"IV: {iv}\nTeks Cipher: {ct}")

def on_decrypt():
    key = key_entry.get().encode('utf-8')
    cipher_text = result_text.get("1.0", tk.END).strip().split('\n')[1].split(': ')[1]
    iv = result_text.get("1.0", tk.END).strip().split('\n')[0].split(': ')[1]

    if len(key) != 8:
        messagebox.showerror("Error", "Kunci harus 8 byte.")
        return

    try:
        plain_text = decrypt(cipher_text, key, iv)
        result_text.delete("1.0", tk.END)
        result_text.insert(tk.END, f"Teks Asli: {plain_text}")
    except Exception as e:
        messagebox.showerror("Error", str(e))

root = tk.Tk()
root.title("DES GUI Sederhana")
root.geometry("400x300")

key_label = tk.Label(root, text="Kunci (8 byte):")
key_label.pack(pady=5)
key_entry = tk.Entry(root, show='*')
key_entry.pack(pady=5)

text_label = tk.Label(root, text="Teks Asli:")
text_label.pack(pady=5)
text_entry = tk.Text(root, height=5, width=40)
text_entry.pack(pady=5)

encrypt_button = tk.Button(root, text="Enkripsi", command=on_encrypt)
encrypt_button.pack(pady=5)

decrypt_button = tk.Button(root, text="Dekripsi", command=on_decrypt)
decrypt_button.pack(pady=5)

result_label = tk.Label(root, text="Hasil:")
result_label.pack(pady=5)
result_text = tk.Text(root, height=5, width=40)
result_text.pack(pady=5)

root.mainloop()