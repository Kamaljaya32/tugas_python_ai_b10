# Tugas 4 - Coding: Python Data Structures

# 1. List – akses & manipulasi

contoh_list = ["apel", 7, "anggur", 4.32, "mangga", 32]
print("List Awal:", contoh_list) # menampilkan list awal

print("Elemen pertama:", contoh_list[0]) # menampilkan elemen pertama
print("Elemen terakhir:", contoh_list[5]) # menampilkan elemen terakhir

print("Slicing [0]:[6]:[2] = ", contoh_list[0:6:2]) # melakukan slicing yang di mana dimulai dri elemen 1 hingga elemen terakhir dengan 2 step

print("Menampilkan list sebelum dilakukan perubahan:", contoh_list) 
contoh_list.append("pisang") # menambahkan item ke dalam list
print("Menampilkan list setelah append pisang:", contoh_list)

contoh_list.insert(2, "jeruk") # insert jeruk ke dalam list pada indeks ke 3
print("Menampilkan list setelah insert jeruk:", contoh_list)

contoh_list.extend(["melon", 99]) # extend item yang berjumlah lebih dari 2 (melon dan 99) ke dalam list
print("Menampilkan list setelah extend melon dan angka 99:", contoh_list)

contoh_list.pop() # pop untuk menghapus item terakhir di dalam list
print("Menampilkan list setelah melakukan pop yg mana akan menghapus item terakhir dalam list:", contoh_list)

contoh_list.remove("jeruk") # menghapus item jeruk dengan menggunakan remove()
print("Menampilkan list setelah melakukan pop yg mana akan menghapus item terakhir dalam list:", contoh_list)

print()

# 2. Tuple – immutability & unpacking

contoh_tuple = ["Kamal", 21, "Teknik Informatika", 2022, "Makassar"] # contoh tuple
print("Menampilkan isi tuple:", contoh_tuple)

print("Menampilkan panjang tuple:", len(contoh_tuple)) # menampilkan panhang tuple
print("Menampilkan indeks kedua dari tuple:", contoh_tuple[1]) # menampilkan indeks kedua dri tuple
print("Menampilan indeks kelima dari tuple:", contoh_tuple[4]) # menampilkan indeks kelima dri tuple

# unpacking tuple
nama = contoh_tuple[0] 
umur = contoh_tuple[1]
asal_daerah = contoh_tuple[4]

print("Nama:", nama)
print("Umur:", umur)
print("Asal daerah:", asal_daerah)

print()

# 3. Set – keunikan & operasi himpunan

a = {1, 2, 3, 4, 4, 5} # angka 4 ada 2
b = {4, 5, 6, 7, 7, 8} # angka 7 ada 2

print("Menampilkan isi Set A:", a) # yang di mana akan menghapus angka 4 yang duplikat
print("Menampilkan isi Set B:", b) # yang di mana akan menghapus angka 7 yang duplikat

print("Menampilkan hasil operasi union:", a | b)
print("Menampilkan hasil operasi intersection:", a & b)
print("Menampilkan hasil operasi difference A-B:", a - b)
print("Menampilkan hasil operasi symmetric difference:", a ^ b)

print()

# 4. Dictionary – key/value dasar

mahasiswa = {
    "nama": "Muhammad Kamal Jaya",
    "nim": "D121221049",
    "angkatan": 2022,
    "kota": "Makassar"
}

print("Data awal mahasiswa:", mahasiswa)

mahasiswa["prodi"] = "Teknik Informatika" # tambah key baru
print("Menampilkan dict setelah menambah data baru", mahasiswa)

mahasiswa["kota"] = "Palu" # mengubah key
print("Menampilkan dict setelah mengubah key (kota):", mahasiswa)

del mahasiswa["angkatan"] # menghapus key
print("Menampilkan dict setelah menghapus angkatan:", mahasiswa)

print("Keys:", mahasiswa.keys()) # tampilkan keys
print("Values:", mahasiswa.values()) # tampilkan values
print("Items:", mahasiswa.items()) # tampilkan items

# iterasi menampilkan key:value
for key in mahasiswa:
    print(key, ":", mahasiswa[key])

print()

# 5. Nested structures

# list 4 buku
buku = [
    {"judul": "Laskar Pelangi", "penulis": "Andrea Hirata", "tahun": 2005},
    {"judul": "Bumi", "penulis": "Tere Liye", "tahun": 2014},
    {"judul": "Atomic Habits", "penulis": "James Clear", "tahun": 2018},
    {"judul": "Negeri 5 Menara", "penulis": "Ahmad Fuadi", "tahun": 2009}
]

# loop untuk print semua judul buku
print("Semua judul buku:")
for i in buku:
    print(i["judul"])

# variabel untuk filter tahun terbit buku 
batas_tahun_terbit = 2010
hasil_filter = [i for i in buku if i["tahun"] >= batas_tahun_terbit] # for loop untuk menyimpan list buku yang sesuai dengan filter

# loop untuk menampilkan buku yang seusai dengan hasil filter
print("Buku tahun >=", batas_tahun_terbit)
for i in hasil_filter:
    print(i)

print()

# 6. Comprehension & utilitas

# Membuat list angka dari 1 sampai 20
angka = list(range(1, 21))

# Membuat list baru yang hanya berisi angka genap
genap = [i for i in angka if i % 2 == 0] # yang di mana angka genap itu sisa bagi = 0

# Membuat list baru yang berisi kuadrat dari setiap angka
kuadrat = [i * i for i in angka]

# Menampilkan hasil
print("Angka genap:", genap)
print("Kuadrat:", kuadrat)

# Membuat dictionary kosong untuk menyimpan status angka
status_angka = {}

# Melakukan perulangan dari 1 sampai 10
for i in range(1, 11):
    # Jika angka habis dibagi 2, maka termasuk genap
    if i % 2 == 0:
        status_angka[i] = "genap"
    # Jika tidak, maka termasuk ganjil
    else:
        status_angka[i] = "ganjil"

# Menampilkan dictionary angka dan statusnya
print("Dictionary genap/ganjil:", status_angka)

# Kalimat yang akan diambil huruf uniknya
kalimat = "Hello World"

# Membuat set huruf unik dalam bentuk lowercase dan tidak mengambil spasi
huruf_unik = {i.lower() for i in kalimat if i != " "}

# Menampilkan hasil huruf unik
print("Huruf unik:", huruf_unik)

print()

# 7. Keanggotaan & pencarian sederhana

# Mengecek apakah kata "apel" ada di dalam list
if "apel" in contoh_list:
    print("apel ada di list")
else:
    print("apel tidak ada di list")

# Mengecek apakah angka 4 ada di dalam set a
if 4 in a:
    print("4 ada di set A")
else:
    print("4 tidak ada di set A")

# Mengecek lagi apakah "apel" ada di list
# Kalau ada, tampilkan posisinya dengan index()
if "apel" in contoh_list:
    print("Posisi apel:", contoh_list.index("apel"))
else:
    print("apel tidak ditemukan")