import tkinter as tk
from tkinter import messagebox

def check_npm():
    nama = entry_nama.get()
    if nama == "Dinda":
        messagebox.showinfo("Hasil", "Npm adalah 130029")
    elif nama == "Rino":
        messagebox.showinfo("Hasil", "Npm adalah 130102")
    else:
        messagebox.showinfo("Hasil", "Nama tidak ditemukan")

# Membuat jendela utama
root = tk.Tk()
root.title("Cek NPM Siswa: ")

# Membuat label dan entry untuk input nama
label_nama = tk.Label(root, text="Inputkan nama siswa:")
label_nama.pack()

entry_nama = tk.Entry(root)
entry_nama.pack()

# Membuat tombol untuk memproses input
button_cek = tk.Button(root, text="Cek NPM", command=check_npm)
button_cek.pack()

# Menjalankan aplikasi
root.mainloop()