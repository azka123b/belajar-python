Materi 7: Perulangan while Loop
Jika for loop digunakan saat kita sudah tahu jumlah pengulangannya, while loop digunakan saat kita tidak tahu kapan harus berhenti. Dia akan terus berjalan selama (while) syaratnya terpenuhi.

1. Cara Kerja while
Bayangkan sebuah mesin yang terus berjalan selama tombol "Emergency Stop" tidak ditekan.
Di Python, strukturnya seperti ini:

Python
pilihan = ""
while pilihan != "stop":
    pilihan = input("Ketik apa saja (atau 'stop' untuk berhenti): ")
    print("Kamu mengetik:", pilihan)
2. Infinite Loop (Hati-hati!)
Jika syaratnya selalu benar (misal: while True:), program tidak akan pernah berhenti kecuali kamu menghentikannya secara paksa (di VS Code tekan Ctrl + C).

3. Keyword break
Kita bisa menghentikan loop secara paksa di tengah jalan menggunakan kata kunci break.