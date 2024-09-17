nama = input("NAMA: ")
nim = input("NIM: ")

harga = int(input("harga beras: "))
diskon_mawar = 11/100
diskon_sania = 14/100
diskon_maknyus = 17/100

besar_diskon_mawar = harga*diskon_mawar
besar_diskon_sania = harga*diskon_sania
besar_diskon_maknyus = harga*diskon_maknyus

beras_mawar = harga - besar_diskon_mawar
beras_sania = harga - besar_diskon_sania
beras_maknyus = harga - besar_diskon_maknyus

print(f"{nama} dengan NIM {nim} ingin membeli beras seharga {harga} ")
print(f"Jika dia membeli beras mawar ia harus membayar {beras_mawar} setelah mendapat diskon 11%")
print(f"Jika dia membeli beras sania ia harus membayar {beras_sania} setelah mendapat diskon 14%")
print(f"Jika dia membeli beras maknyus ia harus membayar {beras_maknyus} setelah mendapat diskon 17%")
