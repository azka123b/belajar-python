# simulasi gerbang otomatis

mahasiswa_lab = ["Azka", "Shafa", "Eka", "Poetra"]

nama_k = input("Masukan Nama Mahasiswa: ")
nama_b = nama_k.strip().title()

if nama_b in mahasiswa_lab:
    print("Akses diterima. Selamat datang", nama_b)
else:
    print("Akses ditolak, nama tidak terdaftar!")