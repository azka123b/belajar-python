Folder 09: Manipulasi String (Merapikan Teks)
Sebagai calon engineer, kamu akan sering berhadapan dengan data input dari sensor atau user yang tidak rapi. Manipulasi string adalah teknik untuk memastikan data teks tersebut sesuai dengan standar yang kita inginkan.

1. Menghapus Spasi "Sampah" (.strip())
Seringkali user tidak sengaja menekan spasi di awal atau akhir kata (misal: "  motor"). Fungsi .strip() akan membuang spasi di ujung kiri dan kanan, tapi tidak membuang spasi di tengah kata.

2. Mengatur Huruf Besar/Kecil
Python sangat peka terhadap perbedaan huruf (case-sensitive). "Admin" tidak sama dengan "admin". Untuk mengatasinya, kita gunakan:

.lower() : Mengubah semua karakter menjadi huruf kecil.

.upper() : Mengubah semua karakter menjadi huruf besar.

.title() : Mengubah huruf pertama setiap kata menjadi huruf besar (seperti penulisan nama).

Contoh Penggunaan dalam Kode:
Python
teks_kotor = "  pOLman BanDung  "

# Kita bersihkan spasi dulu, lalu buat jadi rapi (Title Case)
teks_bersih = teks_kotor.strip().title()

print(f"Sebelum: '{teks_kotor}'")
print(f"Sesudah: '{teks_bersih}'") 
# Hasilnya: 'Polman Bandung'