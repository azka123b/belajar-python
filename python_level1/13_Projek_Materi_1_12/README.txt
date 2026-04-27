# MekatroLog - Smart Inventory System 🤖📦

**MekatroLog** adalah aplikasi manajemen inventaris berbasis terminal yang dirancang khusus untuk mengelola stok komponen di Laboratorium Mekatronika (3AEC). Program ini mengintegrasikan validasi keamanan, manajemen data dinamis, dan analisis statistik sederhana dalam satu antarmuka baris perintah (CLI).

## 🚀 Fitur Utama

- **Security Gate**: Sistem login terenkripsi sederhana dengan validasi username dan password.
- **Dynamic Inventory**: Input data komponen tanpa batas menggunakan perulangan dinamis.
- **Detailed Profiling**: Penyimpanan spesifikasi detail (Nama, Kategori, Harga) menggunakan struktur data Dictionary.
- **Smart Search**: Fitur pencarian barang yang cerdas dan tidak peka terhadap perbedaan huruf besar/kecil (*case-insensitive*).
- **Analytics Dashboard**: Menampilkan total nilai aset, harga tertinggi, dan rata-rata harga komponen secara otomatis.
- **Budget Warning**: Peringatan otomatis jika total nilai aset melebihi ambang batas anggaran (Rp 1.000.000).

## 🛠️ Materi Python yang Diterapkan

Proyek ini merupakan hasil akhir dari pembelajaran dasar pemrograman Python yang mencakup:
1. **Dasar I/O**: `input()` dan `print()` dengan f-string.
2. **Logika Kondisional**: `if`, `elif`, `else` dengan operator logika `and`.
3. **Perulangan**: `while True` dan `for i in range(len())`.
4. **Manipulasi String**: `.strip()`, `.lower()`, dan `.title()`.
5. **Struktur Data**: List untuk stok barang dan Dictionary untuk profil komponen.
6. **Fungsi Built-in**: `len()`, `sum()`, `max()`, dan `round()`.

## 💻 Cara Menjalankan

1. Pastikan Anda sudah menginstal Python 3 di komputer Anda.
2. Clone repositori ini atau download file `.py`-nya.
3. Jalankan perintah berikut di terminal:
   ```bash
   python mekatrolog.py