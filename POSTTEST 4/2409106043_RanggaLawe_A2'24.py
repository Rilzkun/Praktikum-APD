
nama = "rangga"
passw = "43"
salah = 0

while salah < 3:
    username = input("Masukkan username: ")
    password = input("Masukkan password: ")
    if username == nama and password == passw:
        print("Login berhasil!")
        break
    else:
        salah += 1
        print(f"Username atau password salah. Percobaan tersisa: {3 - salah}")

if salah == 3:
    print("Terlalu banyak percobaan. Program akan berhenti.")
else:
    while True:
        nama = input("NAMA: ")
        nim = input("NIM: ")
        pinjaman = int(input("Jumlah pinjaman: "))
        lama_cicilan = input("Lama cicilan (1, 2, atau 3 tahun): ")

        if lama_cicilan == "1":
            bunga_perbulan = (0.07 / 12) * pinjaman
            cicilan_perbulan = (pinjaman + bunga_perbulan) / 12
        elif lama_cicilan == "2":
            bunga_perbulan = (0.13 / 12) * pinjaman
            cicilan_perbulan = (pinjaman + bunga_perbulan) / 24
        elif lama_cicilan == "3":
            bunga_perbulan = (0.19 / 12) * pinjaman
            cicilan_perbulan = (pinjaman + bunga_perbulan) / 36
        else:
            print("Lama cicilan hanya 1-3 tahun.")
            continue  

        print(f"""
NAMA: {nama}
NIM: {nim}
Jumlah pinjaman: {pinjaman}
Lama cicilan: {lama_cicilan} tahun
Cicilan per bulan: {cicilan_perbulan:.2f}
""")

        lanjut = input("Apakah Anda ingin menghitung lagi? (ya/tidak): ")
        if lanjut.lower() != "ya":
            print("Program dihentikan.")
            break
