# Minta pengguna memasukkan modal awal
modal_awal = float(input("Masukkan modal awal (dalam rupiah): "))

# Inisialisasi keuntungan bulanan
keuntungan_bulanan = [0, 0, 0, 0, 0, 0, 0, 0]

# Minta pengguna memasukkan persentase keuntungan untuk bulan ketiga
keuntungan_bulanan[2] = modal_awal * float(input("Masukkan persentase keuntungan bulan ke-3 (%): ")) / 100

# Minta pengguna memasukkan persentase keuntungan untuk bulan kelima
keuntungan_bulanan[4] = modal_awal * float(input("Masukkan persentase keuntungan bulan ke-5 (%): ")) / 100

# Minta pengguna memasukkan persentase keuntungan untuk bulan kedelapan
keuntungan_bulanan[7] = modal_awal * float(input("Masukkan persentase keuntungan bulan ke-8 (%): ")) / 100

# Hitung total keuntungan
total_keuntungan = sum(keuntungan_bulanan)

# Tampilkan hasil
print(f"Total keuntungan selama 8 bulan adalah: {total_keuntungan:.2f}")
