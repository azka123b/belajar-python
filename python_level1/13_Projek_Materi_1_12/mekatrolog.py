#       proyek: Mekatrolog - Smart Inventory System
#   Skenario:
# Kamu diminta membuat sistem terminal untuk mengelola stok komponen 
# di Lab 3AEC. Sistem ini harus bisa memvalidasi user, mencatat komponen, 
# menghitung statistik harga, dan mencari barang secara cerdas.

# 1. Security Gate
while True:
    print("Selamat datang silahkan login terlebih dahulu")
    usern = input("Username: ")
    pw = input("Password: ")

    userr = usern.strip().lower()
    pwr = pw.strip().lower()

    if userr == "azka" and pwr == "polman123":
         print("Login berhasil, selamat datang", usern)
         break
    elif userr == "azka" and pwr != "polman123":
         print("Password Salah!")
    else:
         print("Username tidak terdaftar")

# 2. Dynamic Inventory Input
print("Input Barang ke Gudang")
gudang = []
while True:
     barang = input("Masukan nama barang (ketik 'stop' jika ingin berhenti): ")
     if barang == "stop":
          break
     else:
          barang1 = barang.strip().lower()
          gudang.append(barang1)

# 3. Detailed Component Profiling
barang_terakhir = {
     "nama": barang1,
     "kategori": "",
     "harga": 0
}

print("Masukan detail barang", barang1)
kategori = input("Masukan kategori barang: ")
kategorib = kategori.strip().lower()
barang_terakhir["kategori"] = kategorib
barang_terakhir["harga"] = input("Masukan harga barang: ")

# 4. Smart Search System
print("search untuk mencari nama barang yang sudah di input")
src = input("Masukan nama barang yang mau di cari: ")
srcf = src.strip().lower()
if srcf in gudang:
     print("Ya,",  srcf, "sudah ada dan terdaftar")
else:
     print(srcf, "tidak terdaftar")

# 5. Analystics Dashboard
harga1 = []
print("Masukan harga barang yang sudah di input")
for i in range(len(gudang)):
     harga1.append(int(input(f"Masukan Harga barang {gudang[i]}: ")))

print("Total harga perbarang =", sum(harga1))
if sum(harga1) > 1000000:
     print("PERINGATAN: Total aset melebihi limit anggaran Lab!")
print("Harga barang termahal =", max(harga1))
rata2 = sum(harga1) / len(harga1)
print("Rata-rata dari total barang / harga barang, setelah dibulatkan adalah =", round(rata2))
          
