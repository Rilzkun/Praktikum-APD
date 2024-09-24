nama= input("NAMA: ")
nim= input("NIM: ")
pinjaman= int(input("Jumlah pinjaman: "))
lama_cicilan= input("Lama cicilan 1, 2, atau 3 tahun: ")

if lama_cicilan == "1":
    bunga_perbulan= (0.07/12)*pinjaman
    cicilan_perbulan= int(pinjaman+bunga_perbulan)/12
    print(f"""NAMA: {nama}
NIM: {nim}
Jumlah pinjaman: {pinjaman}
Lama cicilan: {lama_cicilan}
Cicilan perbulan: {cicilan_perbulan}""")
elif lama_cicilan == "2":
    bunga_perbulan= (0.13/12)*pinjaman
    cicilan_perbulan= int(pinjaman+bunga_perbulan)/24
    print(f"""NAMA: {nama}
NIM: {nim}
Jumlah pinjaman: {pinjaman}
Lama cicilan: {lama_cicilan}
Cicilan perbulan: {cicilan_perbulan}""")
elif lama_cicilan == "3":
    bunga_perbulan= (0.19/12)*pinjaman
    cicilan_perbulan= int(pinjaman+bunga_perbulan)/36
    print(f"""NAMA: {nama}
NIM: {nim}
Jumlah pinjaman: {pinjaman}
Lama cicilan: {lama_cicilan}
Cicilan perbulan: {cicilan_perbulan}""")
else:
    print("lama cicilan hanya 1-3 tahun")




    
