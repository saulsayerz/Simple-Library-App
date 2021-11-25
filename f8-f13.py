from utility import *
from datetime import datetime

def search_user_by_id(id) :
# Mencari nama user berdasarkan id pada file users.csv
    
    filename = "data/users.csv"
    data = get_all_to_dictionary(filename)

    found = False
    i = 0
    while (i < len(data) and not(found)) :
        if (data[i]["id"] == id) :
            found = True
            user = data[i]["nama"]
        else :
            i += 1
    
    if (found) :
        return user

def search_gadget_by_id(id) :
# Mencari nama suatu gadget berdasarkan id pada file gadget.csv

    filename = "data/gadget.csv"
    data = get_all_to_dictionary(filename)

    found = False
    i = 0
    while (i < len(data) and not(found)) :
        if (data[i]["id"] == id) :
            found = True
            gadget = data[i]["nama"]
        else :
            i += 1

    if (found) :
        return gadget

def search_consumable_by_id(id) :
# Mencari nama suatu consumable berdasarkan id pada file consumable.csv

    filename = "data/consumable.csv"
    data = get_all_to_dictionary(filename)

    found = False
    i = 0
    while (i < len(data) and not(found)) :
        if (data[i]["id"] == id) :
            found = True
            consumable = data[i]["nama"]
        else :
            i += 1

    if (found) :
        return consumable

def get_id_peminjam_and_id_gadget(id) :
# Mengembalikan id peminjam dan id gadget pada file gadget_borrow_history.csv dalam bentuk tuple
# berdasarkan id peminjaman

    filename = "data/gadget_borrow_history.csv"
    data = get_all_to_dictionary(filename)

    found = False
    i = 0
    while (i < len(data) and not(found)) :
        if (data[i]["id"] == id) :
            found = True
            id_peminjam = data[i]["id_peminjam"]
            id_gadget = data[i]["id_gadget"]
        else :
            i += 1

    return id_peminjam, id_gadget 


def riwayatpinjam() :
# Melihat riwayat peminjaman gadget
# Output : 5 entry terbaru berdasarkan tanggal peminjaman
    
    filename = 'data/gadget_borrow_history.csv'
    # sort_csv_by_key(filename, 'date')       # alternatif 1 buat sort date
    data = get_all_to_dictionary(filename)

    data.sort(key = lambda x: datetime.strptime(x['tanggal_peminjaman'], '%d/%m/%Y'))     # alternatif 2 buat sort date

    # Menampilkan 5 entry dari data paling baru 
    for i in range (-1,-6,-1) :
        print("ID Peminjaman\t\t :", data[i]["id"])
        print("Nama Pengambil\t\t :", search_user_by_id(data[i]["id_peminjam"]))
        print("Nama Gadget\t\t :", search_gadget_by_id(data[i]["id_gadget"]))
        print("Tanggal Peminjaman\t :", data[i]["tanggal_peminjaman"])
        print("Jumlah\t\t\t :", data[i]["jumlah"])
        print()

    # Menawarkan user untuk melihat 5 data lainnya, input yang valid hanya "y" dan "Y"
    c = input("Apakah Anda ingin melihat riwayat tambahan (y/n)? ")
    if (c in "Yy") :     
        idx = -6
        while (c in "Yy") :
            for i in range (idx, (idx-5) ,-1) :
                print("ID Peminjaman\t\t :",  data[i]["id"])
                print("Nama Pengambil\t\t :", search_user_by_id(data[i]["id_peminjam"]))
                print("Nama Gadget\t\t :", search_gadget_by_id(data[i]["id_gadget"]))
                print("Tanggal Peminjaman\t :", data[i]["tanggal_peminjaman"])
                print("Jumlah\t\t\t :", data[i]["jumlah"])
                print()

            c = input("Apakah Anda ingin melihat riwayat tambahan (y/n)? ")
            idx -= 5

def riwayatkembali() :
# Melihat riwayat pengembalian gadget
# Output : 5 entry terbaru berdasarkan tanggal pengambalian
    
    filename = 'data/gadget_return_history.csv'
    # sort_csv_by_key(filename, 'date')       # alternatif 1 buat sort date
    data = get_all_to_dictionary(filename)

    data.sort(key = lambda x: datetime.strptime(x['tanggal_pengembalian'], '%d/%m/%Y'))     # alternatif 2 buat sort date
    
    # Menampilkan 5 entry dari data paling baru 
    for i in range (-1,-6,-1) :
        print("ID Pengembalian\t\t :", data[i]["id"])
        id_peminjam = get_id_peminjam_and_id_gadget(data[i]["id"])[0]
        id_gadget = get_id_peminjam_and_id_gadget(data[i]["id"])[1]
        print("Nama Pengambil\t\t :", search_user_by_id(id_peminjam))
        print("Nama Gadget\t\t :", search_gadget_by_id(id_gadget))
        print("Tanggal Pengembalian\t :", data[i]["tanggal_pengembalian"])
        print()

    # Menawarkan user untuk melihat 5 data lainnya, input yang valid hanya "y" dan "Y"
    c = input("Apakah Anda ingin melihat riwayat tambahan (y/n)? ")
    if (c in "Yy") :     
        idx = -6
        while (c in "Yy") :
            for i in range (idx, (idx-5), -1) :
                print("ID Pengembalian\t\t :", data[i]["id"])
                id_peminjam = get_id_peminjam_and_id_gadget(data[i]["id"])[0]
                id_gadget = get_id_peminjam_and_id_gadget(data[i]["id"])[1]
                print("Nama Pengambil\t\t :", search_user_by_id(id_peminjam))
                print("Nama Gadget\t\t :", search_gadget_by_id(id_gadget))
                print("Tanggal Pengembalian\t :", data[i]["tanggal_pengembalian"])
                print()

            c = input("Apakah Anda ingin melihat riwayat tambahan (y/n)? ")
            idx -= 5

def riwayatambil() :
# Melihat riwayat pengambilan consumable
# Output : 5 entry terbaru berdasarkan tanggal pengambilan consumable

    filename = 'data/consumable_history.csv'
    # sort_csv_by_key(filename, 'date')       # alternatif 1 buat sort date
    data = get_all_to_dictionary(filename)

    data.sort(key = lambda x: datetime.strptime(x['tanggal_pengambilan'], '%d/%m/%Y'))     # alternatif 2 buat sort date

    # Menampilkan 5 entry dari data paling baru 
    for i in range (-1,-6,-1) :
        print("ID Pengembalian\t\t :", data[i]["id"])
        print("Nama Pengambil\t\t :", search_user_by_id(data[i]["id_pengambil"]))
        print("Nama Consumable\t\t :", search_consumable_by_id(data[i]["id_consumable"]))
        print("Tanggal Pengambilan\t :", data[i]["tanggal_pengambilan"])
        print("Jumlah\t\t\t :", data[i]["jumlah"])
        print()

    # Menawarkan user untuk melihat 5 data lainnya, input yang valid hanya "y" dan "Y"
    c = input("Apakah Anda ingin melihat riwayat tambahan (y/n)? ")
    if (c in "Yy") :     
        idx = -6
        while (c in "Yy") :
            for i in range (idx, (idx-5), -1) :
                print("ID Pengembalian\t\t :", data[i]["id"])
                print("Nama Pengambil\t\t :", search_user_by_id(data[i]["id_pengambil"]))
                print("Nama Consumable\t\t :", search_consumable_by_id(data[i]["id_consumable"]))
                print("Tanggal Pengambilan\t :", data[i]["tanggal_pengambilan"])
                print("Jumlah\t\t\t :", data[i]["jumlah"])
                print()

            c = input("Apakah Anda ingin melihat riwayat tambahan (y/n)? ")
            idx -= 5    

def pinjam(userID) :
# Fungsi untuk melakukan peminjaman gadget

    filename = "data/gadget.csv"
    data = get_all_to_dictionary(filename)

    # Menerima input ID
    id = input("Masukan ID item\t\t : ")
    # Memeriksa apakah ID valid atau tidak. Id dikatakan valid jika ID gadget terdapat pada file gadget.csv
    while (id[0] != "G" and mencari_ID(id)[0] == False) : 
        print("ID tidak valid! Periksa kembali ID item")
        id = input("Masukan ID item\t : ")

    # Menerima input tanggal
    tanggal_peminjaman = input("Tanggal Peminjaman (DD/MM/YYYY)\t : ")
    # Memeriksa apakah format tanggal sudah benar
    while (not (is_date_valid(tanggal_peminjaman))) :
        print("Tanggal yang Anda masukkan salah! Format penanggalan adalah DD/MM/YYYY")
        tanggal_peminjaman = input("Tanggal Peminjaman (DD/MM/YYYY)\t : ")
    
    jumlah_peminjaman = int(input("Jumlah Peminjaman\t : "))
    idx_id = mencari_ID(id)[1]  # Indeks pada array data tempat ID gadget berada
    # Memeriksa stok gadget berdasarkan ID gadget
    while (data[idx_id]["jumlah"] < jumlah_peminjaman) :
        print("Jumlah peminjaman melebihi stok pada inventori. Kurangi jumlah peminjaman!")
        jumlah_peminjaman = int(input("Jumlah Peminjaman\t : "))

    data[idx_id]["jumlah"] -= jumlah_peminjaman

    new_data = {'id' : None, 'id_peminjam' : userID , 'id_gadget' : id, 'tanggal_peminjaman' : tanggal_peminjaman, 'jumlah' : jumlah_peminjaman, 'is_returned' : False}
    
    c = input("Apakah Anda yakin ingin meminjam " + data[idx_id]["nama"] + "sebanyak " + jumlah_peminjaman + "buah (y/n)? ")
    if (c in "Yy") :
        if (is_item_returned(userID, id) == False) :
            print("Anda tidak dapat meminjam item yang sama dengan item yang sedang dipinjam")
        else :
            dict_to_csv(filename, data)
            create(new_data, "data/gadget_borrow_history.csv")
            print("Item " + data[idx_id]['nama'] + "(x" + jumlah_peminjaman + ") berhasil dipinjam!")
    else :
        print("Peminjaman item dibatalkan")

def is_item_returned(idUser, idGadget) :
# Memeriksa apakah user sedang meminjam gadget yang sama atau tidak
# Mengembalikan true jika user sedang meminjam gadget yang sama

    filename = "data/gadget_borrow_history.csv"
    data = get_all_to_dictionary(filename)

    isReturned = True
    i = 0

    while (i < len(data) and isReturned == True) :
        if (idUser == data[i]["id_peminjam"]) :
            if (idGadget == data[i]['id_gadget'] and data[i]["is_returned"] == True) :
                i += 1
            else : 
                isReturned = False
        else :
            i += 1

    return isReturned

def is_date_valid(date) :
# Memeriksa apakah format date sudah benar atau belum
# Mengembalikan true jika format tanggal sudah benar

    date_format = "%d/%m/%Y"

    try :
        if date != datetime.strptime(date, date_format).strftime(date_format) :
            raise ValueError
        return True
    except ValueError :
        return False


def minta(userID) :
# Fungsi untuk melakukan permintaan consumable

    filename = "data/consumable.csv"
    data = get_all_to_dictionary(filename)

    id = input("Masukan ID item\t\t : ")
    # Memeriksa apakah ID item valid atau tidak
    while (id[0] != "C" and mencari_ID(id)[0] == False) :
        print("ID tidak valid! Periksa kembali ID item")
        id = input("Masukan ID item\t : ")

    jumlah_permintaan = int(input("Jumlah \t\t : "))
    idx_id = mencari_ID(id)[1]  # Indeks pada array data tempat ID consumable berada
    # Memeriksa stok consumable berdasarkan ID
    while (data[idx_id]["jumlah"] < jumlah_permintaan) :
        print("Jumlah permintaan melebihi stok pada inventori. Kurangi jumlah permintaan!")
        jumlah_permintaan = int(input("Jumlah \t\t : "))    
                
    tanggal_pengambilan = input("Tanggal Permintaan (DD/MM/YYYY)\t : ")
    # Memeriksa apakah format tanggal sudah benar
    while (not (is_date_valid(tanggal_pengambilan))) :
        print("Tanggal yang Anda masukkan salah! Format penanggalan adalah DD/MM/YYYY")
        tanggal_pengambilan = input("Tanggal Permintaan (DD/MM/YYYY)\t : ")

    data[idx_id]["jumlah"] -= jumlah_permintaan

    new_data = {'id' : None, 'id_pengambil' : userID , 'id_consumable' : id, 'tanggal_pengambilan' : tanggal_pengambilan, 'jumlah' : jumlah_permintaan}
    
    dict_to_csv(filename, data)
    create(new_data, "data/consumable_history.csv")
    print("Item " + data[idx_id]['nama'] + "(x" + jumlah_permintaan + ") telah berhasil diambil!")

def kembalikan(userID) :
# Fungsi untuk melakukan pengembalian gadget secara total

    filename = "data/gadget_borrow_history.csv"
    data = get_all_to_dictionary(filename)
    borrowed_gadget = []    # menyimpan list gadget yang sedang dipinjam
                            # index ganjil menyimpan data gadget yang sedang dipinjam, index genap menyimpan nilai index pada array data dari gadget yang sedang dipinjam

    # Mencari list gadget yang sedang dipinjam oleh user
    for i in range (len(data)) :
        if (data[i]["id_peminjam"] == userID and data[i]["is_returned"] == False) :
            borrowed_gadget.append(i)           # menyimpan nilai index pada array data dari gadget yang sedang dipinjam
            borrowed_gadget.append(data[i])     # menyimpan data gadget yang sedang dipinjam

    if (len(borrowed_data) == 0) :
        print("Tidak ada gadget yang sedang dipinjam")
    else :
        num = 1
        for i in range (1, len(borrowed_data), 2) :
            print(num + ". " + search_gadget_by_id(borrowed_gadget[i]["id_gadget"]))
            num += 1

        idx_return = int(input("Masukkan nomor peminjaman\t : "))
        idx_return = 2 * idx_return - 1    
        id_gadget = borrowed_gadget[idx_return]["id_gadget"]     

        tanggal_pengembalian = input("Tanggal Pengembalian (DD/MM/YYYY)\t : ")
        # Memeriksa apakah format tanggal sudah benar
        while (not (is_date_valid(tanggal_pengembalian))) :
            print("Tanggal yang Anda masukkan salah! Format penanggalan adalah DD/MM/YYYY")
            tanggal_pengembalian = input("Tanggal Pengembalian (DD/MM/YYYY)\t : ")

        data[borrowed_gadget[idx_return - 1]]["is_returned"] = True
        dict_to_csv(filename, data)
    
        new_data = {'id' : None, "id_peminjam" : userID, "id_gadget" : id_gadget , "tanggal_pengembalian" : tanggal_pengembalian}
        create(new_data, "data/gadget_return_history.csv")

        print("Item " + search_gadget_by_id(id_gadget) + "(x" + borrowed_gadget[idx_return]['jumlah'] + ") telah dikembalikan")
    

# riwayatpinjam()
# riwayatkembali()
# riwayatambil()
# print(search_user_by_id("2"))
# print(is_date_valid("01/02/1990"))