import os
os.system('cls')
from prettytable import PrettyTable

# Menu perhiasan
data_perhiasan = [
    {"id": 1, "nama": "Cincin Emas", "harga": 500000, "stok": 10},
    {"id": 2, "nama": "Liontin Berlian", "harga": 800000, "stok": 7},
    {"id": 3, "nama": "Gelang Perak", "harga": 300000, "stok": 15}
]

def tampilkan_daftar_perhiasan():
    table_perhiasan = PrettyTable()
    table_perhiasan.field_names = ["ID", "Nama Perhiasan", "Harga (Rp)", "Stok"]
    for perhiasan in data_perhiasan:
        table_perhiasan.add_row([perhiasan["id"], perhiasan["nama"], perhiasan["harga"], perhiasan["stok"]])
    print("Daftar Perhiasan:")
    print(table_perhiasan)

def tambah_perhiasan():
    nama = input("Masukkan Nama Perhiasan: ")
    harga = int(input("Masukkan Harga Perhiasan (Rp): "))
    stok = int(input("Masukkan Jumlah Stok Perhiasan: "))
    new_id = len(data_perhiasan) + 1
    data_perhiasan.append({"id": new_id, "nama": nama, "harga": harga, "stok": stok})
    print("-----Perhiasan berhasil ditambahkan.-----")

def ubah_perhiasan():
    tampilkan_daftar_perhiasan()
    id_perhiasan = int(input("Masukkan ID Perhiasan yang akan diubah: "))
    for perhiasan in data_perhiasan:
        if perhiasan["id"] == id_perhiasan:
            print("Data Perhiasan (ID:", id_perhiasan, "):")
            print("Nama:", perhiasan["nama"])
            print("Harga (Rp):", perhiasan["harga"])
            print("Stok:", perhiasan["stok"])
            perhiasan["nama"] = input("Masukkan Nama Baru: ")
            perhiasan["harga"] = int(input("Masukkan Harga Baru (Rp): "))
            perhiasan["stok"] = int(input("Masukkan Stok Baru: "))
            print("-----Data Perhiasan berhasil diubah.-----")
            return
    print("Maaf Perhiasan dengan ID tersebut tidak ditemukan.")

def hapus_perhiasan():
    tampilkan_daftar_perhiasan()
    id_perhiasan = int(input("Masukkan ID Perhiasan yang akan dihapus: "))
    for perhiasan in data_perhiasan:
        if perhiasan["id"] == id_perhiasan:
            data_perhiasan.remove(perhiasan)
            print("-----Data Perhiasan berhasil dihapus.-----")
            return
    print("Maaf Perhiasan dengan ID tersebut tidak ditemukan.")

def transaksi():
    tampilkan_daftar_perhiasan()
    id_perhiasan = int(input("Masukkan ID Perhiasan yang akan dibeli: "))
    jumlah_beli = int(input("Masukkan jumlah yang akan dibeli: "))

    for perhiasan in data_perhiasan:
        if perhiasan["id"] == id_perhiasan:
            if perhiasan["stok"] >= jumlah_beli:
                total_harga = perhiasan["harga"] * jumlah_beli
                print("-----Transaksi berhasil!-----")
                print("Total harga: Rp", total_harga)
                perhiasan["stok"] -= jumlah_beli
                return
            else:
                print("---Maaf Stok tidak mencukupi.---")
                return
    print("Maaf Perhiasan dengan ID tersebut tidak ditemukan.")

# Fungsi utama untuk menjalankan program
def main():
    while True:
        print("-----Selamat datang di Toko Perhiasan-----")
        print("1. Tampilkan Daftar Perhiasan")
        print("2. Transaksi (Pembeli)")
        print("3. Tambah Perhiasan (Admin)")
        print("4. Ubah Perhiasan (Admin)")
        print("5. Hapus Perhiasan (Admin)")
        print("6. Keluar")
        pilihan = input("Pilihan Anda: ")

        if pilihan == "1":
            tampilkan_daftar_perhiasan()
        elif pilihan == "2":
            transaksi()
        elif pilihan == "3":
            tambah_perhiasan()
        elif pilihan == "4":
            ubah_perhiasan()
        elif pilihan == "5":
            hapus_perhiasan()
        elif pilihan == "6":
            print("---Terima kasih telah menggunakan aplikasi.---")
            break
        else:
            print("---Pilihan tidak valid. Silakan coba lagi.---")

if __name__ == "__main__":
    main()

