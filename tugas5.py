# Tugas 5 - Coding: Python Function and Class

# 1. Function

# fungsi greet untuk membuat sapaan (parameter: nama(string), return: string sapaan)
def greet(nama: str) -> str:
    return "Halo, " + nama + "!"

# fungsi tambah digunakan untuk menjumlahkan 2 angka (parameter -> a = angka pertama; b = angka kedua; nilai default 0.0 kalau tidak diisi)
def tambah(a: float, b: float = 0.0) -> float:
    return a + b

# fungsi rata2 untuk menghitung rata2 dari sebuah list yg berisi angka, jika list kosong fungsi return 0.0, jika tdk hasil rata2 dibulatkan 2 angka di belakang koma
def rata2(angka: list[float]) -> float:
    # mengecek apakah list kosonh
    if len(angka) == 0:
        return 0.0
    total = sum(angka) # menjumlahkan semua isi list
    hasil = total / len(angka) # menghitung rata2

    return round(hasil, 2) # return hasil rata2 dengan 2 angka dibelakang koma

# 2. Class

# membuat class untuk student -> menyimpan data mahasiswa
class Student:
    def __init__(self, nama: str, nim: str, nilai: list[float] = None): # method __init__ akan dipanggil saat objek di buat
        self.nama = nama # nama mahasiswa
        self.nim = nim # nim mahasiswa

        # jika nilai tidak diisi, maka akan buat list kosong
        if nilai is None:
            self.nilai = []
        else:
            self.nilai = nilai
    
    # method untuk menambahkan satu nilai ke dalam list nilai
    def tambah_nilai(self, skor: float):
        self.nilai.append(skor)

    # menthod untuk menghitung nilai rata2 mahasiswa
    def rata_nilai(self) -> float:
        return rata2(self.nilai) # menggunakan fungsi rata2 yg sdh dibuat di atas
    
    # menthod untuk menentukan status kelulusan
    def status(self, threshold: float = 70.0) -> str:
        if self.rata_nilai() >= threshold:
            return "LULUS"
        else:
            return "TIDAK LULUS"
    
    # method __str__ digunakan untuk objek mahasiswa bisa dicetak dengan print
    def __str__(self):
        return f"Student(nama:'{self.nama}', nim:'{self.nim}', rata:{self.rata_nilai()}, status:{self.status()})"
    
# 3. Demo

if __name__ == "__main__":
    print("=== FUNCTIONS ===")

    # memanggil fungsi greet
    print(greet("Arifian"))

    # memanggil fungsi tambah
    print("tambah(5, 7) =", tambah(5,7))
    print("tambah(10) =", tambah(10))

    # memanggil fungsi rata2
    print("rata2([80, 90, 100]) =", rata2([80, 90, 100]))
    print("rata([]) =", rata2([]))

    print("\n=== CLASS STUDENT ===")

    # membuat objek mahasiswa 1
    mahasiswa1 = Student("Asep", "A123")
    mahasiswa1.tambah_nilai(80)
    mahasiswa1.tambah_nilai(85)
    mahasiswa1.tambah_nilai(90)

    # membuat objek mahasiswa 2
    mahasiswa2 = Student("Budi", "B123")
    mahasiswa2.tambah_nilai(60)
    mahasiswa2.tambah_nilai(70)
    mahasiswa2.tambah_nilai(65)

    # print mahassiswa 1
    print(mahasiswa1)
    print("Rata-rata:", mahasiswa1.rata_nilai())
    print("Status:", mahasiswa1.status())

    print()

    # print mahasiswa 2
    print(mahasiswa2)
    print("Rata-rata:", mahasiswa2.rata_nilai())
    print("Status:", mahasiswa2.status())