# Tugas Pemrograman Python Infinte Learning: Data Structures, OOP, & Data Analysis

Repositori ini berisi implementasi kode dari Tugas 4, 5, dan 6 yang membangun pemahaman mengenai bahasa pemrograman Python. Mulai dari manipulasi data dasar, perancangan struktur kode berbasis Pemrograman Berorientasi Objek (OOP), hingga pengolahan data menggunakan library eksternal.

## Daftar Tugas

### [Tugas 4] Python Data Structures
Fokus pada eksplorasi dan manipulasi struktur data bawaan (*built-in*) Python untuk menyimpan dan mengelola data:
* **List:** Akses, *slicing*, dan manipulasi memori (`append`, `insert`, `extend`, `pop`, `remove`).
* **Tuple:** Memahami sifat *immutability* (tidak dapat diubah) dan teknik *unpacking* nilai.
* **Set:** Penyimpanan data unik dan operasi himpunan matematika (*Union, Intersection, Difference, Symmetric Difference*).
* **Dictionary:** Pengelolaan data berbasis *Key-Value* dan teknik iterasinya.
* **Comprehension & Nested Structure:** Pembuatan (*list of dictionaries*) dan penulisan *looping* bersyarat yang ringkas.

### [Tugas 5] Python Function and Class
Menerapkan konsep modularitas dan Pemrograman Berorientasi Objek (OOP) agar kode lebih terstruktur, rapi, dan dapat digunakan ulang (*reusable*):
* **Function:** Mendefinisikan fungsi (`def`) dengan parameter, nilai *default*, dan anotasi tipe data (*type hinting*) untuk menangani logika spesifik.
* **Class:** Pembuatan kelas `Student` sebagai *blueprint* data mahasiswa. Mengelola atribut (nama, NIM, nilai), serta implementasi berbagai *method* khusus (`__init__`, evaluasi status kelulusan, dan *magic method* `__str__`).

### [Tugas 6] Data Analysis & File I/O (NumPy & Pandas)
Mengintegrasikan konsep OOP dengan *library* standar industri untuk analisis data, serta pengoperasian sistem file:
* **NumPy:** Menghasilkan data secara acak (*random generator*) dan menghitung statistik deskriptif dasar (rata-rata, median, standar deviasi, min/max).
* **Pandas:** Mengonversi data mentah menjadi *DataFrame*, memanipulasi kolom, dan mengevaluasi status kelulusan massal dengan fungsi `.apply(lambda)`.
* **File I/O:** Membaca dan menulis laporan statistik ke file eksternal (`.txt`) menggunakan *context manager* (`with open(...)`).
* **OOP Terintegrasi:** Membangun kelas `GradeBook` yang membungkus *DataFrame* Pandas sebagai alat pengelola nilai dan pembuat laporan otomatis.

## Persyaratan Sistem & Instalasi

1. Pastikan **Python 3.x** sudah terinstal di perangkat Anda.
2. Instal library yang dibutuhkan (khusus Tugas 6) dengan menjalankan perintah berikut di terminal/command prompt:
   ```bash
   pip install numpy pandas
