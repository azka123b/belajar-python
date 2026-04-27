# simulasi login
user = input("Masukan Username: ")
pas = input("Masukan Password: ")

if user == "admin" and pas == "admin123":
    print("Login Berhasil!")
elif user == "admin" and pas != "admin123":
    print("Login Gagal, Password salah!")
else:
    print("Login Gagal, Username tidak terdaftar")

