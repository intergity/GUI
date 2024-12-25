import tkinter as tk
from tkinter import messagebox

def on_button_click():
    user_input = entry.get()
    messagebox.showinfo("Informasi", f"Anda memasukkan: {user_input}")

root = tk.Tk()
root.title("Chipergui - Aplikasi GUI Sederhana")
root.geometry("300x200")

label = tk.Label(root, text="Masukkan sesuatu:")
label.pack(pady=10)

entry = tk.Entry(root)
entry.pack(pady=10)

button = tk.Button(root, text="Kirim", command=on_button_click)
button.pack(pady=10)

root.mainloop()