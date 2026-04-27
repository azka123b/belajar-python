Materi 8: Python Lists (Daftar Data)
Sejauh ini, satu variabel hanya bisa menyimpan satu data (contoh: nama = "Azka"). Tapi bagaimana jika kita punya 100 nama komponen mesin? Tidak mungkin kita buat 100 variabel. Di sinilah kita butuh List.

1. Cara Membuat List
List menggunakan kurung siku [] dan datanya dipisahkan dengan koma.

Python
komponen = ["Motor DC", "Sensor IR", "Arduino", "Kabel"]
2. Cara Mengambil Data (Index)
Di dunia pemrograman, urutan dimulai dari 0, bukan 1.

komponen[0] -> "Motor DC"

komponen[2] -> "Arduino"

3. Menambah Data
Kita bisa menambah data ke dalam list menggunakan fungsi .append().

Python
komponen.append("Baterai") # Menambahkan Baterai ke urutan paling akhir