Folder 10: Membership Operators (in dan not in)
Sekarang kita masuk ke materi yang sangat berguna untuk melakukan pencarian data dengan cepat. Dalam mekatronika, ini sering dipakai untuk mengecek apakah sebuah ID sensor atau nama perintah ada dalam daftar yang diizinkan.

1. Apa itu Membership Operator?
Operator ini digunakan untuk menguji apakah suatu nilai atau variabel ada di dalam sebuah urutan (seperti String, List, atau Tuple). Hasilnya selalu berupa Boolean (True atau False).

in: Menghasilkan True jika nilai ditemukan di dalam urutan.

not in: Menghasilkan True jika nilai TIDAK ditemukan di dalam urutan.

2. Kenapa Ini Penting?
Tanpa operator ini, kamu harus menggunakan for loop untuk membongkar isi list satu per satu hanya untuk mencari satu kata. Dengan in, Python melakukannya untukmu dalam satu baris kode.

Contoh Logika:
Python
daftar_izin = ["azka", "kaa", "admin"]
user = "azka"

if user in daftar_izin:
    print("Akses Diterima")
else:
    print("Akses Ditolak")