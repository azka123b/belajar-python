#   Struktur Logika:
#   if: Kondisi pertama yang dicek.
#   elif: Dicek hanya jika kondisi sebelumnya salah. Kamu bisa punya banyak elif.
#   else: Dijalankan jika semua kondisi di atas salah.

#   contoh
skor = 7
if skor >= 90:
    print("Grade A")
elif skor >= 80:
    print("Grade B")
elif skor >= 70:
    print("Grade C")
else:
    print("Grade D (Tidak lulu!)")