def cek_berat(bs, target):
    if bs < target:
        selisih = target - bs
    else:
        selisih = bs - target
    return selisih

print("Ini aplikasi untuk menghitung berat badan sekarang dan target")
bsi = int(input("Masukan berat badan saat ini: "))
targeti = int(input("Masukan berat badan target: "))

if bsi == targeti:
    print("Selamat!, Target telah tercapai")
else:
    selisihi = cek_berat(bsi, targeti)
    print("Semangat!, kurang", selisihi, "KG lagi untuk capai target")