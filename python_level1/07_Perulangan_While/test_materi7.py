status = ""
while status != "off":
    status = input("Masukan perintah (on/off): ")
    if status == "on":
        print("Mesin berjalan normal")
    elif status == "off":
        print("Mesin dimatikan. Program selesai!")
    else:
        print("Printah salah!")