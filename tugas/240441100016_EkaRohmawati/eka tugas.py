# Input data
print("Di suatu hari terdapat dua orang anak yang sedang akan membeli sesuatu ditoko")
nama1 =input("masukkan nama anak pertama : ")
nama2 =input("masukkan nama anak kedua : ")
print(nama1, f": {nama2} kamu mau beli apa?")
print(nama2, f": aku mau beli bolpoin , kalo kamu mau beli apa?")
print(nama1, f": aku sih beli kertas")
print(nama2, f": pak ini harganya berapa ya?")
print(f"pak penjual : untuk bolpoinnya harganya Rp 5000 perbuah, kalo untuk kertasnya Rp 1000 perlembar")
jumlah1 = int(input("masukkan jumlah bolpoin : "))
jumlah2 = int(input("masukkan jumlah kertas : "))

# Operasi aritmatika
print(f"pak penjual : Semua totalnya Rp {jumlah1*5000 + jumlah2*1000}")
print(nama2, f": iya pak ini uangnya")
print(f"pak pejual : oh iya dek terimakasih")

# logika
print(f"apakah kertas lebih banyak dari bolpoin??? {jumlah2 > jumlah1}")

print(f"mereka pun akhirnya pulang bersama")




