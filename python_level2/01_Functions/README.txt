Materi 01: Functions (Fungsi) - Si "Tombol Otomatis"
Dalam pemrograman, Function adalah blok kode yang kita bungkus agar bisa digunakan berulang kali. Bayangkan seperti membuat Macro atau Sub-routine pada PLC atau Robot Controller.

1. Struktur Dasar def
Untuk membuat fungsi, kita gunakan kata kunci def (singkatan dari define).

Python
def sapa_operator():
    print("Sistem KUKA KRC2 Aktif")
    print("Status: Ready to Move")

# Cara memanggilnya:
sapa_operator()
2. Parameter (Input untuk Fungsi)
Fungsi akan jauh lebih berguna jika kita bisa mengirimkan data ke dalamnya. Data ini disebut Parameter.

Python
def kontrol_motor(kecepatan, arah):
    print(f"Motor berputar ke arah {arah} dengan speed {kecepatan} RPM")

# Memanggil dengan input berbeda
kontrol_motor(1500, "Clockwise")
kontrol_motor(500, "Counter-Clockwise")
3. Return Value (Hasil Balikan)
Kadang kita tidak ingin fungsi cuma nge-print, tapi ingin fungsi itu menghitung sesuatu dan memberikan hasilnya kembali ke kita. Gunakan kata kunci return.

Python
def hitung_tegangan(arus, hambatan):
    v = arus * hambatan
    return v # Hasil perhitungan dikirim keluar

# Hasil disimpan ke variabel
voltase = hitung_tegangan(2, 110)
print(f"Tegangan yang dibutuhkan: {voltase} Volt")