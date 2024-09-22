import tkinter as tk
from tkinter import messagebox

def cek_nilai():
    try:
        nilai = int(entry_nilai.get())
        if 100 >= nilai >= 86:
            keterangan = "Sangat Baik"
        elif 85 >= nilai >= 76:
            keterangan = "Baik"
        elif 75 >= nilai >= 66:
            keterangan = "Cukup"
        elif 65 >= nilai >= 56:
            keterangan = "Kurang"
        else:
            keterangan = "Gagal"
        messagebox.showinfo("Hasil", f"Nilai: {nilai}, Keterangan: {keterangan}")
    except ValueError:
        messagebox.showerror("Error", "Input harus berupa angka")

# Membuat jendela utama
root = tk.Tk()
root.title("Cek Nilai Siswa")

# Membuat label dan entry untuk input nilai
label_nilai = tk.Label(root, text="Inputkan Nilai:")
label_nilai.pack()

entry_nilai = tk.Entry(root)
entry_nilai.pack()

# Membuat tombol untuk memproses input
button_cek = tk.Button(root, text="Cek Nilai", command=cek_nilai)
button_cek.pack()

# Menjalankan aplikasi
root.mainloop()