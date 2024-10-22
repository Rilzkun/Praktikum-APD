lowongan_kerja = []  
id_counter = 1  
total_lowongan = 0  

def tambah_lowongan():  
    global id_counter, total_lowongan  
    pekerjaan = input("Masukkan jenis pekerjaan: ")
    perusahaan = input("Masukkan nama perusahaan: ")
    lokasi = input("Masukkan lokasi: ")
    gaji = input("Masukkan gaji: ")

    lowongan = {
        'id': id_counter,
        'pekerjaan': pekerjaan,
        'perusahaan': perusahaan,
        'lokasi': lokasi,
        'gaji': gaji
    }
    lowongan_kerja.append(lowongan)
    id_counter += 1
    total_lowongan += 1  
    print("Lowongan kerja berhasil ditambahkan!")

def tampilkan_lowongan():  
    print("\nKoleksi Lowongan Kerja:")
    if not lowongan_kerja:
        print("Belum ada lowongan tersedia.")
        return
    for job in lowongan_kerja:
        print(f"{job['id']}: {job['pekerjaan']} di {job['perusahaan']} ({job['lokasi']}, Gaji: {job['gaji']})")

def perbarui_lowongan(job_id):  
    ditemukan = False
    
    for job in lowongan_kerja:
        if job['id'] == job_id:
            pekerjaan_baru = input("Masukkan jenis pekerjaan baru: ")
            perusahaan_baru = input("Masukkan nama perusahaan baru: ")
            lokasi_baru = input("Masukkan lokasi baru: ")
            gaji_baru = input("Masukkan gaji baru: ")
            
            job['pekerjaan'] = pekerjaan_baru
            job['perusahaan'] = perusahaan_baru
            job['lokasi'] = lokasi_baru
            job['gaji'] = gaji_baru
            ditemukan = True
            print("Lowongan kerja berhasil diperbarui!")
            break
    
    if not ditemukan:
        print("Lowongan tidak ditemukan!")

def hapus_lowongan(job_id):  
    global total_lowongan  
    for job in lowongan_kerja:
        if job['id'] == job_id:
            lowongan_kerja.remove(job)
            total_lowongan -= 1  
            print("Lowongan kerja berhasil dihapus!")
            return
    print("Lowongan tidak ditemukan!")  

def tampilkan_menu():  
    print("\nMenu:")
    print("1. Tambah Lowongan Kerja")  
    print("2. Tampilkan Semua Lowongan Kerja")  
    print("3. Perbarui Lowongan Kerja")  
    print("4. Hapus Lowongan Kerja")  
    print("5. Tampilkan Total Lowongan")  
    print("6. Keluar")  

def tampilkan_total_lowongan():  
    print(f"Total lowongan saat ini: {total_lowongan}")  

def jalankan_program():  
    while True:
        tampilkan_menu()  
        pilihan = input("Pilih opsi (1-6): ")

        if pilihan == '1':
            tambah_lowongan()  
        elif pilihan == '2':
            tampilkan_lowongan()  
        elif pilihan == '3':
            job_id = int(input("Masukkan ID lowongan yang ingin diperbarui: "))  
            perbarui_lowongan(job_id)  
        elif pilihan == '4':
            job_id = int(input("Masukkan ID lowongan yang ingin dihapus: ")) 
            hapus_lowongan(job_id)  
        elif pilihan == '5':
            tampilkan_total_lowongan()  
        elif pilihan == '6':
            print("Keluar dari program.") 
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.") 

jalankan_program()  
