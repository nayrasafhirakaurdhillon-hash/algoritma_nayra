# 1. input data: input nama barang dan jumlah stok awal
print("=== SISTEM PENGELOLAAN STOK BARAMG TOKO ===")
nama_barang = input("masukkan nama barang ")
stok = int(input("masukkan jumlah stok: "))

# 5. perulangan melakukan transaksi berkali kali
while True:
    print(f"\nbarang: {nama_barang} | stok saat ini: {stok}")
    print("pilih transaksi: ")
    print("1. barang masuk ")
    print("2. barang keluar ")
    print("3. selesai")

    # 2. pilih transaksi
    pilihan = input("masukkan pilihan (1/2/3): ")

    # 3. proses transaksi menggunakan percabangan
    if pilihan == "1" :
        jumlah_masuk = int(input("masukkan jumlah barang masuk: "))
        stok += jumlah_masuk
        print(f"Berhasil menambahkan {jumlah_masuk} {nama_barang}.")
        

    elif pilihan == "2":
        jumlah_keluar = int(input("masukkan jumlah barang keluar"))

        # 4.cek stok: memeriksa ketersediaan stok
        if jumlah_keluar > stok:
            print("stok tidak mencukupi")
        else:
            stok -= jumlah_keluar
            print(f"berhasil mengurangi {jumlah_keluar} {nama_barang}. ")
    elif pilihan == "3":
        # keluar dari perulangan jika transaksi seleai
        break
    else:
        print("pilihan tidak valid. silakan pilih 1,2, atau 3. ")

# 6. tampilkan hasil: jumlah stok terakhir setelah transaksi selesai
print("\=== HASIL AKHIR TRANSAKSI ===")
print(F"Nama barang : {nama_barang} ")
print(f"stok terakhir: {stok}")