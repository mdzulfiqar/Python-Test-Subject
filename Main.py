# Sintaks sekuensial
print("Hello World")
nama = "M. Dzulfiqar Tanggono"
usia = 19
print(nama, "Usia=", usia)

# Sintaks bercabang
if usia >= 19:
    print("Masih muda")
    print("Usia belajar")
    print("Usia mencari jati diri")
else:
    print("Tidak muda")
    print("Banyakin Tobat")
    print("Pikir keluarga")

# Sintaks Perulangan
jumlah_anak = 2
for iterasi in range(1, jumlah_anak+1):
    print("Halo anak ke", iterasi)

# contoh_lain: menghitung 1+2+3+4+5
jumlah_bilangan = 5
total_penjumlahan = 0
for bilangan in range(1, jumlah_bilangan+1):
    total_penjumlahan = total_penjumlahan + bilangan

print("Hasil penjumlahan", total_penjumlahan)

# tipe data array
uang_untuk_anak = [] # tipe data array
uang_untuk_anak.append(10000)
uang_untuk_anak.append(5000)
uang_untuk_anak.append(50000)

# berapa rata2 uang untuk tiap anak
jumlah_total_uang = 0
for uang in uang_untuk_anak:
    jumlah_total_uang = jumlah_total_uang + uang

print("Jumlah total uang", jumlah_total_uang)
rata_rata_uang = jumlah_total_uang / 3
print("Rata-rata uang", rata_rata_uang)