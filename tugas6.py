# Import library yang dibutuhkan
import numpy as np
import pandas as pd
import os

# Mengatur seed agar data untuk random tetap konsisten
np.random.seed(42)

# membuat class GradeBook agar dapat mengelola data nilai mahasiswa
class GradeBook:
    def __init__(self, df: pd.DataFrame):
        self.df = df # df _> dataframe untuk menyimpan data mahasiswa

    # method untuk menghitung rata2 nilai dari kolom "nilai"
    def rata2(self) -> float:
        return round(self.df["nilai"].mean(), 2)
    
    # method untuk menghitung persentase mahasiswa lulus, default threshold 70
    def lulus(self, threshold: float = 70.0) -> float:
        jumlah_lulus = (self.df["nilai"] >= threshold).sum()
        total_data = len(self.df)

        if total_data == 0:
            return 0.0
        
        persentase = (jumlah_lulus / total_data) * 100
        return round(persentase, 2)
    
    # method untuk menyimpan ringkasan ke file txt
    def ringkasan(self, path: str):
        jumlah_data = len(self.df)
        jumlah_lulus = (self.df["status"] == "LULUS").sum()
        jumlah_tidak_lulus = (self.df["status"] == "TIDAK LULUS").sum()

        with open(path, "a", encoding="utf-8") as file:
            file.write("\n=== RINGKASAN DARI CLASS GRADEBOOK ===\n")
            file.write(f"Jumlah data        : {jumlah_data}\n")
            file.write(f"Rata-rata nilai    : {self.rata2()}\n")
            file.write(f"Persentase lulus   : {self.lulus()}%\n")
            file.write(f"Jumlah lulus       : {jumlah_lulus}\n")
            file.write(f"Jumlah tidak lulus : {jumlah_tidak_lulus}\n")
    
    # method __str__ untuk cetak objek dengan printf()
    def __str__(self):
        return f"GradeBook(jumlah_data={len(self.df)}, rata_rata={self.rata2})"

# main program
if __name__ == "__main__":
    # NUMPY
    print("=== NUMPY ===")

    # membuat array numpy berisi nilai ujian minimal dengan 10 data
    nilai_ujian = np.random.randint(50, 101, size=10)

    # menghitung statistik dasar dengan numpy
    rata = np.mean(nilai_ujian)
    median = np.median(nilai_ujian)
    std_dev = np.std(nilai_ujian)
    nilai_min = np.min(nilai_ujian)
    nilai_max = np.max(nilai_ujian)

    # menampilkan array dan hasil statistik
    print("Nilai ujian:", nilai_ujian)
    print("Rata-rata:", round(rata, 2))
    print("Median:", round(median, 2))
    print("Standar deviasi:", round(std_dev, 2))
    print("Nilai minimum:", nilai_min)
    print("Nilai maksimum:", nilai_max)

    # PANDAS
    print("\n=== PANDAS ===")

    # membuat dataframe dengan 5 baris dan mengambil nilai dari sebagian array numpy yg sdh dibuat
    data = {
        "nama": ["Budi", "Siti", "Andi", "Rina", "Dewi"],
        "nim": ["A101", "A102", "A103", "A104", "A105"],
        "nilai": nilai_ujian[:5]
    }

    df = pd.DataFrame(data)

    # menambahkan kolom status berdasarkan nilai dengan treshold 70
    df["status"] = df["nilai"].apply(lambda x: "LULUS" if x >= 70 else "TIDAK LULUS")

    # menampilkan 5 baris pertama datarame
    print(df.head())

    # FILE I/O
    # menyimpan ringkasan statistik dan dataframe ke file txt
    nama_file = "ringkasan_tugas6.txt"

    jumlah_baris = len(df)
    jumlah_lulus = (df["status"] == "LULUS").sum()
    jumlah_tidak_lulus = (df["status"] == "TIDAK LULUS").sum()

    with open(nama_file, "w", encoding="utf-8") as file:
        file.write("=== RINGKASAN STATISTIK NUMPY ===\n")
        file.write(f"Nilai ujian        : {nilai_ujian.tolist()}\n")
        file.write(f"Rata-rata          : {round(rata, 2)}\n")
        file.write(f"Median             : {round(median, 2)}\n")
        file.write(f"Standar deviasi    : {round(std_dev, 2)}\n")
        file.write(f"Nilai minimum      : {nilai_min}\n")
        file.write(f"Nilai maksimum     : {nilai_max}\n")

        file.write("\n=== RINGKASAN DATAFRAME ===\n")
        file.write(f"Jumlah baris       : {jumlah_baris}\n")
        file.write(f"Jumlah lulus       : {jumlah_lulus}\n")
        file.write(f"Jumlah tidak lulus : {jumlah_tidak_lulus}\n")

    # OOP: GRADEBOOK
    print("\n=== OOP: GRADEBOOK ===")

    # membuat objek gradebook dari dataframe
    gb = GradeBook(df)

    # menampilkan isi ringkas objek
    print(gb)

    # menampilkan rata-rata nilai
    print("Rata-rata:", gb.rata2())

    # menampilkan persentase kelulusan
    print("Persentase Kelulusan", gb.lulus(), "%")

    # menyimpan ringkasan tambahan dari class gradebook ke file yang sama
    gb.ringkasan(nama_file)

    # menampilkan lokasi file ringkasan
    print(f"Ringkasan berhasil disimpan ke file: {os.path.abspath(nama_file)}")

