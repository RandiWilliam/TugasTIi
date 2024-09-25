# Meminta input jumlah belanja dari pengguna
jumlah_belanja = float(input("Masukkan jumlah belanja: "))

# Mengecek apakah jumlah belanja lebih dari 300
if jumlah_belanja > 300:
    # Menghitung diskon 15%
    diskon = jumlah_belanja * 0.15
    total_belanja = jumlah_belanja - diskon
    print(f"Anda mendapat diskon 15%. Total belanja setelah diskon: {total_belanja}")
else:
    # Tidak ada diskon
    total_belanja = jumlah_belanja
    print(f"Anda tidak mendapat diskon. Total belanja: {total_belanja}")
