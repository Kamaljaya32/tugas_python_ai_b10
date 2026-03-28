# Tugas 3 - Coding: Python Basics

# 1. Deklarasi Variabel dan Tipe Data

nama = "Muhammad Kamal Jaya" # string
umur = 21 # integer
tinggi = 170.5 # float
mahasiswa_aktif = True # boolean
hobi = ["Main Game", "Futsal", "Tidur"] #list

# menampilkan isi variabel
print("Nama:", nama)
print("Umur:", umur)
print("Tinggi badan:", tinggi)
print("Mahasiswa aktif:", mahasiswa_aktif)
print("Hobi:", hobi)

print()

# 2. Manipulasi String
print("Aku Suka Main Game Football Manager :)") # menampilkan teks menggunakan printf()

nama_depan = "Muhammad Kamal"
nama_belakang = "Jaya"

nama_lengkap = nama_depan + " " + nama_belakang # menggabungkan string
print("Nama Lengkap:", nama_lengkap)

print("Panjang nama lengkap:", len(nama_lengkap)) # menghitung panjang string
print("Nama dalam Huruf Besar:", nama_lengkap.upper()) # mengubah nama lengkap menjadi huruf besar
print("Nama dalam Huruf Besar:", nama_lengkap.lower()) # mengubah nama lengkap menjadi huruf kecil

print()

# 3. Operasi Matematika 
a = 10
b = 4

print("Pertambahan:", a + b) # operasi pertambahan
print("Pengurangan:", a - b) # operasi pengurangan
print("Perkalian:", a * b) # operasi perkalian
print("Pembagian:", a / b) # operasi pembagian
print("Pembagian dengan hasil bulat:", a // b) # operasi pembagian dengan hasil bulat
print("Sisa bagi/modulus:", a % b) # operasi sisa bagi/modulus

print()

# 4. List dan Akses Elemen
warna = ["Merah", "Putih", "Hitam", "Hijau", "Biru"]
print("List warna:", warna) # menampilkan isi list


print("Warna Ketiga:", warna[2]) # menampilkan elemen tertentu
print("Warna Kelima:", warna[4]) # menampilkan elemen tertentu

warna.append("Kuning") # menambah item baru
print("List Warna setelah ditambah warna baru:", warna)

warna.remove("Hitam") # menghapus item dengan remove() yang di mana akan menghapus warna hitam
print("List Warna setelah dihapus warna Hitam:", warna)

warna.pop() # menghapus item dengan pop() -> menghapus item terakhir dalam list
print("List Warna setelah dihapus warna terakhir dalam list:", warna)

print()

# 5. Penggunaan Input dari User

nama_user = input("Masukkan nama Anda: ")
umur_user = input("Masukkan umur Anda: ")

print("Halo, nama saya " + nama_user + " dan umur saya " + umur_user + " tahun")