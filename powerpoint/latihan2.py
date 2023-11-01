# Meminta pengguna untuk memasukkan data
data1 = float(input("Masukkan data pertama: "))
data2 = float(input("Masukkan data kedua: "))
data3 = float(input("Masukkan data ketiga: "))

# Menggunakan sorted() untuk mengurutkan data
sorted_data = sorted([data1, data2, data3])

# Menampilkan hasil pengurutan
print("Data terurut secara berurutan:")
for item in sorted_data:
    print(item)
