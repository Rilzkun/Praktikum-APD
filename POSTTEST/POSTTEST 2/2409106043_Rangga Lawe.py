#memasukkan nama dan nim
nama = input("NAMA: ")
nim = input("NIM: ")

#menentukan diskon semua merek
harga = int(input("harga beras: "))
diskon_mawar = 0.11
diskon_sania = 0.14
diskon_maknyus = 0.17

#menghitung besar diskon
besar_diskon_mawar = harga*diskon_mawar
besar_diskon_sania = harga*diskon_sania
besar_diskon_maknyus = harga*diskon_maknyus

#menghitung harga setelah diskon
beras_mawar = harga - besar_diskon_mawar
beras_sania = harga - besar_diskon_sania
beras_maknyus = harga - besar_diskon_maknyus

#output
print(f"{nama} dengan NIM {nim} ingin membeli beras seharga {harga} ")
print(f"Jika dia membeli beras mawar ia harus membayar {beras_mawar} setelah mendapat diskon 11%")
print(f"Jika dia membeli beras sania ia harus membayar {beras_sania} setelah mendapat diskon 14%")
print(f"Jika dia membeli beras maknyus ia harus membayar {beras_maknyus} setelah mendapat diskon 17%")
