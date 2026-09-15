produk = {
    "nama": "sabun muka",
    "harga": 38000,
    "stok": 30
}

def tampilkan_data():
    print("\n=== data produk ===")
    for key, value in produk.items():
        print(f"{key.capitalize()} : {value}")

def tambah_kategori():
    kategori = input("masukkan kategori produk: ")
    produk["kategori"] = kategori
    print(f"kategori '{kategori}' berhasil ditambahkan.")

def ubah_harga():
    if "harga" in produk:
        harga_baru = input(f"harga saat ini: {produk['harga']}. masukkan harga baru: ")
        try:
            produk["harga"] = int(harga_baru)
            print("harga berhasil ditubah.")
        except ValueError:
            print("input harga tidak valid! harus berupa angka.")
    else:
        print("data harga tidak ditemukan.")

def hapus_kategori():
    if "kategori" in produk:
        del produk["kategori"]
        print("kategori berhasil dihapus.")
    else:
        print("kategori tidak ditemukan dalam data produk.")

while True:
    print("\n===== menu pengelolaan data produk =====")
    print("1. tampilkan data produk")
    print("2. tambah kategori produk")
    print("3. ubah harga produk")
    print("4. hapus kategori produk")
    print("5. keluar")

    pilihan = input("pilih menu (1-5): ")

    if pilihan == "1":
        tampilkan_data()

    elif pilihan == "2":
        tambah_kategori()

    elif pilihan == "3":
        ubah_harga()
        tampilkan_data()

    elif pilihan == "4":
        hapus_kategori()
        tampilkan_data()

    elif pilihan == "5":
        print("terima kasih telah menggunakan program ini.")
        break

    else:
        print("pilihan tidak valid! silahkan menu 1-5.")
