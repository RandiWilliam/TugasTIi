import tkinter as tk
from tkinter import messagebox

def hitung_diskon():
    try:
        total_belanja = int(entry_belanja.get())
    except ValueError:
        messagebox.showerror("Input Error", "Masukkan nilai yang valid!")
        return

    diskon = 0
    bonus = ""

    if total_belanja > 500000:
        diskon = total_belanja * 0.07  # Diskon 7%
        bonus = "Mug Cantik"
    elif 100000 <= total_belanja <= 499000:
        diskon = total_belanja * 0.05  # Diskon 5%
        bonus = "Coca Cola"
    elif total_belanja < 100000:
        bonus = "Kupon Potongan Belanja"

    total_setelah_diskon = total_belanja - diskon

    # Menampilkan hasil dengan message box
    result_message = (
        f"Total Belanja: Rp{total_belanja}\n"
        f"Diskon: Rp{diskon}\n"
        f"Bonus: {bonus}\n"
        f"Total yang harus dibayar: Rp{total_setelah_diskon}"
    )
    messagebox.showinfo("Hasil Perhitungan", result_message)

# Membuat window Tkinter
root = tk.Tk()
root.title("Penghitung Diskon dan Bonus")

# Label dan Entry untuk Total Belanja
label_belanja = tk.Label(root, text="Masukkan Total Belanja (Rp):")
label_belanja.pack(pady=10)

entry_belanja = tk.Entry(root)
entry_belanja.pack(pady=5)

# Tombol untuk menghitung diskon
button_hitung = tk.Button(root, text="Hitung Diskon dan Bonus", command=hitung_diskon)
button_hitung.pack(pady=20)

# Menjalankan aplikasi
root.mainloop()