import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image

def encode_image(image_path, message):
    image = Image.open(image_path)
    encoded_image = image.copy()
    width, height = image.size

    message_length = len(message)
    if message_length > 255:
        raise ValueError("Pesan terlalu panjang! Maksimal 255 karakter.")

    encoded_image.putpixel((0, 0), (message_length, 0, 0))

    index = 0
    for y in range(height):
        for x in range(width):
            if index < message_length:
                r, g, b = image.getpixel((x, y))
                char = message[index]
                encoded_image.putpixel((x, y), (ord(char), g, b))
                index += 1
            else:
                break
        if index >= message_length:
            break

    return encoded_image

def decode_image(image_path):
    image = Image.open(image_path)
    width, height = image.size
    message_length = image.getpixel((0, 0))[0]
    message = ""

    for y in range(height):
        for x in range(width):
            r, g, b = image.getpixel((x, y))
            if len(message) < message_length:
                message += chr(r)
            else:
                break
        if len(message) >= message_length:
            break

    return message

def sembunyikan_pesan():
    image_path = filedialog.askopenfilename(title="Pilih Gambar", filetypes=[("File Gambar", "*.png;*.jpg;*.jpeg")])
    if not image_path:
        return

    message = message_entry.get("1.0", tk.END).strip()
    if not message:
        messagebox.showerror("Error", "Pesan tidak boleh kosong!")
        return

    try:
        encoded_image = encode_image(image_path, message)
        save_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])
        if save_path:
            encoded_image.save(save_path)
            messagebox.showinfo("Sukses", "Pesan berhasil disembunyikan dalam gambar!")
    except Exception as e:
        messagebox.showerror("Error", str(e))

def tampilkan_pesan():
    image_path = filedialog.askopenfilename(title="Pilih Gambar", filetypes=[("File Gambar", "*.png;*.jpg;*.jpeg")])
    if not image_path:
        return

    try:
        message = decode_image(image_path)
        messagebox.showinfo("Pesan Tersembunyi", f"Pesan: {message}")
    except Exception as e:
        messagebox.showerror("Error", str(e))

root = tk.Tk()
root.title("SteganoGUI Sederhana")
root.geometry("400x300")

message_label = tk.Label(root, text="Masukkan Pesan:")
message_label.pack(pady=5)
message_entry = tk.Text(root, height=5, width=40)
message_entry.pack(pady=5)

hide_button = tk.Button(root, text="Sembunyikan Pesan", command=sembunyikan_pesan)
hide_button.pack(pady=5)

reveal_button = tk.Button(root, text="Tampilkan Pesan", command=tampilkan_pesan)
reveal_button.pack(pady=5)

root.mainloop()