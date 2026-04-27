# Struktur dasar
# untuk membuat fungsi menggunakan kata kunci 'def'
def salam_s():
    print("Selamat Pagi/Siang/Sore/Malam")
    print("Bagaimana hari mu?")

salam_s()

# parameter
def kontrol(kecepatan, arah):
    print(f"Motor berputar ke arah {arah} dengan kecepatan {kecepatan} RPM")

kontrol(2000, "kiri")
kontrol(1220, "kanan")

# Return (hasil dikirim keluar)
def hitung_tegangan(arus, hambatan):
    v = arus * hambatan
    return v # untuk mengirim hasil v keluar

arus = int(input("Masukan arus: "))
hambatan = int(input("Masukan nilai hambatan: "))

volt = hitung_tegangan(arus, hambatan)
print("Tegangan yang dibutuhkan:", volt, "Volt")