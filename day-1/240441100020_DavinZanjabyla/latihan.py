nama = "Davin Zanjabyla A"
nim = 240441100020
ipk = 4.00
mahasiswa = True

print("Nama saya adalah", nama)
# ini adalah format natural (tipe data sama)
print("Nim saya adalah", nim)
print("Impian Ipk saya adalah", ipk)
print("Saya merupakan Mahasiswa", mahasiswa)

# ini adalah format string (tipe data di ubah menjadi string)
print(f'Nim saya adalah {nim}')

# program dinamis string
nama_panjang = str(input("Nama saya adalah : "))

# program dinamis integer
nilai_matematika = int(input("Nilai saya adalah : "))

nilai_matematika = 89
nilai_fisika = 75
nilai_biologi = 90
nilai_kimia = 82

penjumlaha = nilai_matematika + nilai_kimia
pengurangan = nilai_matematika - nilai_kimia
perkalian = nilai_matematika * nilai_kimia
pembagian = nilai_matematika / nilai_kimia

print(f'Hasil penjumlahan dari matematika dan kimia adalah : {penjumlaha}')
print(f'Hasil pengurangan dari matematika dan kimia adalah : {pengurangan}')
print(f'Hasil pembagian dari matematika dan kimia adalah : {pembagian}')
print(f'Hasil perkalian dari matematika dan kimia adalah : {perkalian}')

usia_masuk_kuliah = int(input("Berapa usia anda saat masuk kuliah ?"))
lama_kuliah = int(input("Berapa lama anda kuliah (tahun) ?"))

usia_saat_ini = usia_masuk_kuliah + lama_kuliah
tahun_lulus = 2024 + lama_kuliah

print(f'Saat ini, saya {nama} berumur {usia_saat_ini}')
print(f'Saya {nama} akan lulus pada tahun {tahun_lulus}')