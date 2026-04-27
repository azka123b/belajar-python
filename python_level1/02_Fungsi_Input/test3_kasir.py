#program kasir sederhana
nama_barang = input("Masukan nama barang yang kamu beli: ")
harga_barang = int(input("Masukan harga barang anda: "))
jumlah_barang = int(input("Masukan jumlah barang yang anda beli: "))
total_harga = harga_barang * jumlah_barang

print("Anda membeli", nama_barang, "sebanyak", jumlah_barang, "pcs")
print("Total harga yang harus di bayar adalah:", total_harga)