#   for loop
# for loop digunakan ketika kita tahu persis berapa kali kita ingin 
# mengulang sesuatu. Di Python, kita sering menggunakan fungsi range() 
# untuk menentukan jumlah perulangannya.

#   Fungsi range()
# range(5) artinya akan mengulang sebanyak 5 kali 
# (dimulai dari angka 0 sampai 4).

#range(1, 6) artinya mulai dari angka 1 sampai 5 
# (angka terakhir tidak diikutkan).

#   contoh
print("Menghitung 1-5")
for i in range(1, 6):
    print("Angka ke-", i)