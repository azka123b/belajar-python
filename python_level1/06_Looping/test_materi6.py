# menghitung keliling likaran dengan 3 jari jari yang berbeda
for i in range(1, 4):
    # fungsi f adalah untuk memasukan variabel kedalam text selain di print
    jari_jari = int(input(f"Masukan jari-jari ke-{i}: "))
    keliling = 2 * 3.14 * jari_jari
    print("Hasil dari jari-jari ke-", i,":", keliling)