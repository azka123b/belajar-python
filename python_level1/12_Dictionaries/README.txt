Folder 12: Dictionaries (Data Berlabel)
Sejauh ini kamu sudah belajar List untuk menyimpan banyak data. Tapi List punya kelemahan: datanya hanya punya urutan (0, 1, 2...), kita tidak tahu itu data apa kalau tidak melihat isinya.

Dictionary (Kamus) memungkinkan kita menyimpan data dengan sistem Key: Value (Kunci: Nilai). Ini mirip seperti identitas mahasiswa; ada label "Nama", "NIM", dan "Jurusan".

1. Cara Membuat Dictionary
Menggunakan kurung kurawal {}.

Python
# Format -> kunci: nilai
mahasiswa = {
    "nama": "Azka",
    "nim": 223443074,
    "prodi": "Mekatronika"
}
2. Cara Mengambil Data
Bukan pakai angka indeks, tapi panggil kuncinya.

mahasiswa["nama"] -> Hasilnya: "Azka"

3. Mengubah atau Menambah Data
Sangat mudah, tinggal panggil kuncinya lalu isi nilai baru.

mahasiswa["semester"] = 6 # Menambahkan kunci baru

mahasiswa["nama"] = "Kaa" # Mengubah data yang sudah ada