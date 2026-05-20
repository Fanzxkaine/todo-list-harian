# --- PROGRAM KASIR KANTIN ---
print("=== SELAMAT DATANG DI KANTIN DIGITAL ===")

# Ini bagian input data
harga = int(input("Masukkan Harga Makanan: "))
jumlah = int(input("Beli Berapa Banyak?   : "))

# Ini bagian hitung-hitungan
total = harga * jumlah
print("Total Belanjaan Lu: Rp", total)

# Ini bagian pembayaran
bayar = int(input("Uang Lu Berapa?       : "))
kembalian = bayar - total

# Ini bagian logika (Keputusan)
if kembalian > 0:
    print("Kembalian lu: Rp", kembalian)
elif kembalian == 0:
    print("Uang pas ya, mantap!")
else:
    print("Uang lu kurang: Rp", abs(kembalian))
    print("Nggak bisa ngutang ya!")

print("========================================")