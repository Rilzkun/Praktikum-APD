# Menyimpan koleksi lowongan kerja dalam list
lowongan_kerja = []
id = 1

while True:
    # Menampilkan menu
    print("\nMenu:")
    print("1. Tambah Lowongan Kerja")
    print("2. Tampilkan Semua Lowongan Kerja")
    print("3. Perbarui Lowongan Kerja")
    print("4. Hapus Lowongan Kerja")
    print("5. Keluar")
    
    pilihan = input("Pilih opsi (1-5): ")
    
    if pilihan == '1':
        pekerjaan = input("Masukkan jenis pekerjaan: ")
        perusahaan = input("Masukkan nama perusahaan: ")
        lokasi = input("Masukkan lokasi: ")
        gaji = input("Masukkan gaji: ")
        
        # Menambahkan lowongan kerja baru
        lowongan = {
            'id': id,
            'pekerjaan': pekerjaan,
            'perusahaan': perusahaan,
            'lokasi': lokasi,
            'gaji': gaji
        }
        lowongan_kerja.append(lowongan)
        id += 1
        print("Lowongan kerja berhasil ditambahkan!")
    
    elif pilihan == '2':
        # Menampilkan semua lowongan kerja
        print("\nKoleksi Lowongan Kerja:")
        for job in lowongan_kerja:
            print(f"{job['id']}: {job['pekerjaan']} di {job['perusahaan']} ({job['lokasi']}, Gaji: {job['gaji']})")
    
    elif pilihan == '3':
        job_id = int(input("Masukkan ID lowongan yang ingin diperbarui: "))
        ditemukan = False
        
        # Memperbarui lowongan kerja
        for job in lowongan_kerja:
            if job['id'] == job_id:
                job['pekerjaan'] = input("Masukkan jenis pekerjaan: ")
                job['perusahaan'] = input("Masukkan nama perusahaan baru: ")
                job['lokasi'] = input("Masukkan lokasi baru: ")
                job['gaji'] = input("Masukkan gaji baru: ")
                ditemukan = True
                print("Lowongan kerja berhasil diperbarui!")
                break
        
        if not ditemukan:
            print("Lowongan tidak ditemukan!")
    
    elif pilihan == '4':
        job_id = int(input("Masukkan ID lowongan yang ingin dihapus: "))
        
        # Menghapus lowongan kerja
        lowongan_kerja = [job for job in lowongan_kerja if job['id'] != job_id]
        print("Lowongan kerja berhasil dihapus!")
    
    elif pilihan == '5':
        print("Keluar dari program.")
        break
    
    else:
        print("Pilihan tidak valid. Silakan coba lagi.")
