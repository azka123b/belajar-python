# simulasi daftar inventaris
gudang = []
while True:
    barang = input("Masukan nama barang (ketik 'selesai' untuk stop): ")
    if barang == "selesai":
        break
    else:
        gudang.append(barang)
print("Isi gudang saat ini ada", gudang)