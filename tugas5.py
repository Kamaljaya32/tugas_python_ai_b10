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

