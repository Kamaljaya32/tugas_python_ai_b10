# Import library yang dibutuhkan
import numpy as np
import pandas as pd
import os

# Mengatur seed agar data untuk random tetap konsisten
np.random.seed(42)

# membuat class GradeBook agar dapat mengelola data nilai mahasiswa
class GradeBook:
    def __int__(self, df: pd.DataFrame):
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