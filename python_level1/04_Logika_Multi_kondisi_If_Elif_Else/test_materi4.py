# mesin pengecek suhu laptop
suhu = int(input("Masukan suhu laptop saat ini: "))

if suhu > 80:
    print("Suhu saat ini masuk kategori Overheat!")
elif suhu > 60:
    print("Suhu Sudah mulai tinggi")
else:
    print("Suhu dalam kondini normal dan aman")