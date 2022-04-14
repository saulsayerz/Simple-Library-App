from utility import *
from datetime import datetime
from os import system, chdir

# File ini merupakan semua fungsi utama pada F03 -- F13, F15 -- F17, dan bonus FB02

# CATATAN: 
# is returned akan true jika dan hanya jika semuanya telah dikembalikan
def carirarity(folder_name, gadget) :
    rarity = input("Masukkan rarity: ").title()
    cari = {"rarity" : rarity}
    clean = search(folder_name + '/gadget.csv', gadget, cari) #memanfaatkan fungsi yang sudah ada
    
    print()
    
    if len(clean) == 0:
        print("Data kosong")
        return
    
    print("Hasil pencarian: ")
    print()

    for i in range (len(clean)) : # Untuk mencetak tiap data dari data clean yang berarti ada rarity yang diminta
        print("Nama            :", clean[i]["nama"])
        print("Deskripsi       :", clean[i]["deskripsi"])
        print("Jumlah          :", clean[i]["jumlah"])
        print("Rarity          :", clean[i]["rarity"])
        print("Tahun Ditemukan :", clean[i]["tahun_ditemukan"])
        print()
        print()
    return
#carirarity(folder_name)

def caritahun(folder_name, gadget) :
    tahun = int(input("Masukkan tahun: "))
    kategori = input("Masukkan kategori: ")
    print()
    print("Hasil pencarian: \n")
    bersih = []
    kotor = gadget # Apabila kategori ada, dan mencari hal yang diinginkan di kategori
    
    if kotor == []:
        print("Tidak ada data")
        return

    for i in range (len(kotor)) : # Untuk mencari mana data yang sesuai dengan tahun dan kategori yang diminta
        if kategori == "=" :
            if int(kotor[i]['tahun_ditemukan']) == tahun :
                bersih.append(kotor[i])
        if kategori == ">" :
            if int(kotor[i]['tahun_ditemukan']) > tahun :
                bersih.append(kotor[i])
        if kategori == "<" :
            if int(kotor[i]['tahun_ditemukan']) < tahun :
                bersih.append(kotor[i])
        if kategori == ">=" :
            if int(kotor[i]['tahun_ditemukan']) >= tahun :
                bersih.append(kotor[i])
        if kategori == "<=" :
            if int(kotor[i]['tahun_ditemukan']) <= tahun :
                bersih.append(kotor[i])
    for i in range (len(bersih)) : # Untuk mencetak tiap data dari data bersih yang berarti tahun dan kategori
        print("Nama            :", bersih[i]["nama"])
        print("Deskripsi       :", bersih[i]["deskripsi"])
        print("Jumlah          :", bersih[i]["jumlah"])
        print("Rarity          :", bersih[i]["rarity"])
        print("Tahun Ditemukan :", bersih[i]["tahun_ditemukan"])
        print()
        print()
    if len(bersih) == 0:
        print('Tidak ada data ditemukan')
    return
#CONTOH APLIKASI caritahun(filename) :
#caritahun('data/gadget.csv')



def tambahitem(folder_name, gadget, consumable) :
    ID = input("Masukan ID: ")
    if (ID[0] != 'G' and ID[0] != 'C') : # Untuk mengecek apakah ID sudah sesuai format atau tidak
        print("Gagal menambahkan item karena ID tidak valid.") 
        return '', None
    else :
        id_ada = mencari_id(ID, gadget, consumable, folder_name)[0] #Mencari ID apakah ada atau tidak dengan fungsi yang sudah dibuat
        if id_ada == True :
            print("Gagal menambahkan item karena ID sudah ada.") # Mencetak demikian apabila data sudah ada
            return '', None
        else :
            nama = input("Masukan Nama: ")
            if ID[0] == 'G':
                cari = search(folder_name + '/gadget.csv', gadget, {'nama': nama})
                if cari != []:
                    print("Error: Nama gadget sudah ada")
                    return '', None
            else:
                cari = search(folder_name + '/consumable.csv', consumable, {'nama': nama})
                if cari != []:
                    print("Error: Nama consumable sudah ada")
                    return '', None
            deskripsi = input("Masukan Deskripsi: ")
            jumlah = int(input("Masukan Jumlah: "))
            if jumlah < 0 :
                print("input jumlah tidak valid!") #Karena jumlah stok tidak bisa negatif
                return '', None
            rarity = input("Masukan Rarity: ").title()
            if rarity != 'C' and rarity != 'B' and rarity != 'A' and rarity !='S' : 
                print("input rarity tidak valid!") # Untuk rarity yang tidak valid
                return '', None
            if ID[0] == 'G' : # Untuk kasus ID adalah gadget
                tahun = input("Masukan tahun ditemukan: ") #asumsi tahun negatif = sebelum masehi
                data_baru = {'id': ID[1:], 'nama': nama, 'deskripsi': deskripsi, 'jumlah': str(jumlah), 'rarity': rarity, 'tahun_ditemukan': tahun}
                print("Item telah berhasil ditambahkan ke database")
                gadget.append(data_baru)
                return 'gadget', gadget
            else : # Untuk kasus ID adalah consumable
                data_baru = {'id': ID[1:], 'nama': nama, 'deskripsi': deskripsi, 'jumlah': str(jumlah), 'rarity': rarity}
                print("Item telah berhasil ditambahkan ke database")
                consumable.append(data_baru)
                return 'consumable', consumable


def hapusitem(folder_name, gadget, consumable) :
    ID = input("Masukan ID item: ")
    id_ada = mencari_id(ID, gadget, consumable, folder_name)[0] # Mengecek apakah ID ada atau tidak menggunakan fungsi yang sudah ada
    if id_ada == False or (ID[0] != 'G' and ID[0] != 'C') :
        print("Tidak ada item dengan ID tersebut!")
        return '', None
    else : # Untuk kasus itemnya ada
        jenis = ''
        urutan_id = mencari_id(ID, gadget, consumable, folder_name)[1]
        if ID[0] =='G' : # Mengambil data gadget
            jenis = 'gadget'
            data = gadget
        else : # Mengambil data consumable
            jenis = 'consumable'
            data = consumable
        yakin = input("Apakah anda yakin ingin menghapus " + data[urutan_id]['nama']+ " (Y/N)? ")

        if yakin == "Y" or yakin == 'y' : #Apabila memilih yakin
            data.pop(urutan_id)
            print("Item telah berhasil dihapus dari database.")
            return jenis, data

        else : #Apabila memilih tidak yakin untuk dibatalkan
            print("Penghapusan item dibatalkan.")
            return jenis, data
        
#hapusitem()


def ubahjumlah(folder_name, gadget, consumable) :
    ID = input("Masukan ID: ")
    id_ada = mencari_id(ID, gadget, consumable, folder_name)[0] # Mengecek apakah ID ada atau tidak menggunakan fungsi yang sudah ada
    if id_ada == False or (ID[0] != 'G' and ID[0] != 'C') :
        print("Tidak ada item dengan ID tersebut!")
        return '', None
    else : # Untuk kasus bahwa ID ada
        urutanID = mencari_id(ID, gadget, consumable, folder_name)[1]
        if ID[0] == 'G' : #Untuk mencari di data Gadget
            data = gadget
            stok_awal = data[urutanID]['jumlah']
        else : #Untuk mencari data di consumable
            data = consumable
            stok_awal = data[urutanID]['jumlah']
        jumlah = int(input("Masukan Jumlah: "))
        if int(stok_awal) + jumlah < 0 : # Apabila stoknya menjadi negatif karena kebuang terlalu banyak
            print(abs(jumlah), data[urutanID]['nama'], 'gagal dibuang karena stok kurang. Stok sekarang:', stok_awal, "(<", str(jumlah*-1) + ")")
            return '', None
        else : #Untuk kasus stoknya tetap valid
            data[urutanID]['jumlah'] = str(int(stok_awal) + jumlah)
            if ID[0] == 'G' : 
                print(jumlah, data[urutanID]['nama'], "berhasil ditambahkan. Stok sekarang:", str(int(stok_awal)+jumlah))
                return 'gadget', data
            else :
                print(jumlah, data[urutanID]['nama'], "berhasil ditambahkan. Stok sekarang:", str(int(stok_awal)+jumlah))
                return 'consumable', data

# ubahjumlah()

    
def save(consumable, consumable_history, gadget, gadget_borrow_history, gadget_return_history, users, folder_name):
    folder_tujuan = input("Masukkan nama folder penyimpanan: ")
    print("Saving...")
    

    belum_ada = 1
    if not os.path.isdir(folder_tujuan):
        system('mkdir ' + folder_tujuan)
        belum_ada = 0

    # copy data

    header = [
        'id;nama;deskripsi;jumlah;rarity',
        'id;id_pengambil;id_consumable;tanggal_peminjaman;jumlah',
        'id;nama;deskripsi;jumlah;rarity;tahun_ditemukan',
        'id;id_peminjam;id_gadget;tanggal_peminjaman;jumlah;is_returned',
        'id;id_peminjam;id_gadget;tanggal_pengembalian;jumlah_pengembalian',
        'id;username;nama;alamat;password;role'
    ]


    bulk_write(consumable, folder_name, folder_tujuan, 'consumable.csv', belum_ada, header[0])
    bulk_write(consumable_history, folder_name, folder_tujuan, 'consumable_history.csv', belum_ada, header[1])
    bulk_write(gadget, folder_name, folder_tujuan, 'gadget.csv', belum_ada, header[2])
    bulk_write(gadget_borrow_history, folder_name, folder_tujuan, 'gadget_borrow_history.csv', belum_ada, header[3])
    bulk_write(gadget_return_history, folder_name, folder_tujuan, 'gadget_return_history.csv', belum_ada, header[4])
    bulk_write(users, folder_name, folder_tujuan, 'user.csv', belum_ada, header[5])

    print("Data telah disimpan pada folder " + folder_tujuan + '!')

def help():
    print("register -> (admin only) mendaftarkan pengguna baru dengan level akses 'user'")
    print("tambahitem -> (admin only) menambahkan gadget baru ke dalam inventory")
    print("hapusitem -> (admin only) menghapus gadget atau consumable")
    print("ubahjumlah -> (admin only) mengubah jumlah gadget atau consumable pada inventory")
    print("riwayatpinjam -> (admin only) melihat riwayat peminjaman gadget")
    print("riwayatkembali -> (admin only) melihat riwayat pengembalian gadget")
    print("pinjam -> (user only) meminjam gadget")
    print("kembalikan -> (user only) mengembalikan gadget")
    print("minta -> (user only) meminta consumable")
    print("riwayatambil -> (admin only) melihat riwayat pengambilan consumables")
    print("carirarity -> mencari gadget berdasarkan rarity")
    print("caritahun -> mencari gadget berdasarkan tahun ditemukan")
    print("save -> menyimpan data dalam sebuah folder")
    print("help -> menampilkan list perintah beserta level aksesnya")
    print("exit -> keluar dari program")

def keluar(consumable, consumable_history, gadget, gadget_borrow_history, gadget_return_history, users, folder_name):
    pilihan = input("Apakah anda mau melakukan penyimpanan file yang sudah diubah ? (y/n) ")
    if pilihan == 'y' or pilihan == 'Y':
        save(consumable, consumable_history, gadget, gadget_borrow_history, gadget_return_history, users, folder_name)
    else:
        print("Perubahan tidak disimpan")

def riwayatpinjam(folder_name, gadget_borrow_history, gadget, users) :
# Melihat riwayat peminjaman gadget
# Output : 5 entry terbaru berdasarkan tanggal peminjaman
    
    data = gadget_borrow_history
    filename = folder_name + '/gadget_borrow_history.csv'
    filename_user = folder_name + '/user.csv'
    filename_gadget = folder_name + '/gadget.csv'
    data.sort(key = lambda x: datetime.strptime(x['tanggal_peminjaman'], '%d/%m/%Y'))     # alternatif 2 buat sort date
    data.reverse()

    if len(data) == 0:
        print("Tidak ada data yang dapat ditampilkan")
        return
        
    # Menampilkan 5 entry dari data paling baru 
    banyak_ditampilkan = min(len(data), 5)
    
    for i in range (banyak_ditampilkan):
        
        id_peminjam = search(filename, gadget_borrow_history, {'id_peminjam': data[i]["id_peminjam"]})[0]['id_peminjam']
        peminjam = search(filename_user, users, {'id': id_peminjam})[0]['nama']

        id_gadget = search(filename, gadget_borrow_history, {'id_gadget': data[i]["id_gadget"]})[0]['id_gadget']
        gadget_yang_dipinjam = search(filename_gadget, gadget, {'id': id_gadget})[0]['nama']

        print("ID Peminjaman\t\t :", data[i]["id"])
        print("Nama Pengambil\t\t :", peminjam)
        print("Nama Gadget\t\t :", gadget_yang_dipinjam)
        print("Tanggal Peminjaman\t :", data[i]["tanggal_peminjaman"])
        print("Jumlah\t\t\t :", data[i]["jumlah"])
        print()

    # Menawarkan user untuk melihat 5 data lainnya, input yang valid hanya "y" dan "Y"
    if len(data) <=5:
        return

    c = input("Apakah Anda ingin melihat riwayat tambahan (y/n)? ")
    if (c in "Yy") :     
        
        last = False
        idx = 5

        while (c in "Yy") and not last :

            if idx+5 > len(data):
                jarak = len(data)
                last = True
            else:
                jarak = 5+idx

            for i in range (idx, jarak) :

                id_peminjam = search(filename, gadget_borrow_history, {'id_peminjam': data[i]["id_peminjam"]})[0]['id_peminjam']
                peminjam = search(filename_user, users, {'id': id_peminjam})[0]['nama']

                id_gadget = search(filename, gadget_borrow_history, {'id_gadget': data[i]["id_gadget"]})[0]['id_gadget']
                gadget_yang_dipinjam = search(filename_gadget, gadget, {'id': id_gadget})[0]['nama']

                print("ID Peminjaman\t\t :",  data[i]["id"])
                print("Nama Pengambil\t\t :", peminjam)
                print("Nama Gadget\t\t :", gadget_yang_dipinjam)
                print("Tanggal Peminjaman\t :", data[i]["tanggal_peminjaman"])
                print("Jumlah\t\t\t :", data[i]["jumlah"])
                print()

            if not last:
                c = input("Apakah Anda ingin melihat riwayat tambahan (y/n)? ")
                idx += 5


def riwayatkembali(folder_name, gadget_return_history, gadget, users) :
# Melihat riwayat pengembalian gadget
# Output : 5 entry terbaru berdasarkan tanggal pengambalian
    

    data = gadget_return_history

    if len(data) == 0:
        print("Tidak ada data yang dapat ditampilkan")
        return

    data.sort(key = lambda x: datetime.strptime(x['tanggal_pengembalian'], '%d/%m/%Y'))     # alternatif 2 buat sort date
    data.reverse()

    filename = folder_name + '/gadget_return_history.csv'
    filename_user = folder_name + '/user.csv'
    filename_gadget = folder_name + '/gadget.csv'

    # Menampilkan 5 entry dari data paling baru 
    banyak_ditampilkan = min(len(data), 5)
    for i in range (banyak_ditampilkan) :

        id_peminjam = search(filename, gadget_return_history, {'id_peminjam': data[i]["id_peminjam"]})[0]['id_peminjam']
        peminjam = search(filename_user, users, {'id': id_peminjam})[0]['nama']

        id_gadget = search(filename, gadget_return_history, {'id_gadget': data[i]["id_gadget"]})[0]['id_gadget']
        gadget_yang_dikembalikan = search(filename_gadget, gadget, {'id': id_gadget})[0]['nama']

        print("ID Pengembalian\t\t :", data[i]["id"])
        print("Nama Pengambil\t\t :", peminjam)
        print("Nama Gadget\t\t :", gadget_yang_dikembalikan)
        print("Tanggal Pengembalian\t :", data[i]["tanggal_pengembalian"])
        print("Jumlah Kembalian\t :", data[i]["jumlah_pengembalian"])
        print()

    # Menawarkan user untuk melihat 5 data lainnya, input yang valid hanya "y" dan "Y"
    if len(data) <=5:
        return

    c = input("Apakah Anda ingin melihat riwayat tambahan (y/n)? ")
    if (c in "Yy") :
        last = False
        idx = 5

        while (c in "Yy") and not last :
            if idx+5 > len(data):
                jarak = len(data)
                last = True
            else:
                jarak = 5+idx

            for i in range (idx, jarak) :
                id_peminjam = search(filename, get_gadget_return_history, {'id_peminjam': data[i]["id_peminjam"]})[0]['id_peminjam']
                peminjam = search(filename_user, users, {'id': id_peminjam})[0]['nama']

                id_gadget = search(filename, gadget_return_history, {'id_gadget': data[i]["id_gadget"]})[0]['id_gadget']
                gadget_yang_dikembalikan = search(filename_gadget, gadget, {'id': id_gadget})[0]['nama']

                print("ID Pengembalian\t\t :", data[i]["id"])
                print("Nama Pengambil\t\t :", peminjam)
                print("Nama Gadget\t\t :", gadget_yang_dikembalikan)
                print("Tanggal Pengembalian\t :", data[i]["tanggal_pengembalian"])
                print("Jumlah Pengembalian\t :", data[i]["jumlah_pengembalian"])
                print()

            if not last:
                c = input("Apakah Anda ingin melihat riwayat tambahan (y/n)? ")
                idx += 5

def riwayatambil(folder_name, consumable_history, consumable, users) :
# Melihat riwayat pengambilan consumable
# Output : 5 entry terbaru berdasarkan tanggal pengambilan consumable

    filename = folder_name + '/consumable_history.csv'
    filename_user = folder_name + '/user.csv'
    filename_consumable = folder_name + '/consumable.csv'

    data = consumable_history
    if len(data) == 0:
        print("Tidak ada data yang dapat ditampilkan")
        return

    data.sort(key = lambda x: datetime.strptime(x['tanggal_pengambilan'], '%d/%m/%Y'))     # alternatif 2 buat sort date
    data.reverse()

    # Menampilkan 5 entry dari data paling baru 

    banyak_ditampilkan = min(len(data), 5)
    for i in range (banyak_ditampilkan) :
        
        id_pengambil = search(filename, consumable_history, {'id_pengambil': data[i]["id_pengambil"]})[0]['id_pengambil']
        pengambil = search(filename_user, users, {'id': id_pengambil})[0]['nama']

        id_consumable = search(filename, consumable_history, {'id_consumable': data[i]["id_consumable"]})[0]['id_consumable']
        consumable_yang_diambil = search(filename_consumable, consumable, {'id': id_consumable})[0]['nama']

        print("ID Pengembalian\t\t :", data[i]["id"])
        print("Nama Pengambil\t\t :", pengambil)
        print("Nama Consumable\t\t :", consumable_yang_diambil)
        print("Tanggal Pengambilan\t :", data[i]["tanggal_pengambilan"])
        print("Jumlah\t\t\t :", data[i]["jumlah"])
        print()

    # Menawarkan user untuk melihat 5 data lainnya, input yang valid hanya "y" dan "Y"

    if len(data) <=5:
        return

    c = input("Apakah Anda ingin melihat riwayat tambahan (y/n)? ")
    if (c in "Yy") :     
        last = False
        idx = 5

        while (c in "Yy") and not last :
            if idx+5 > len(data):
                jarak = len(data)
                last = True
            else:
                jarak = 5 + idx

            for i in range (idx, jarak) :
                id_pengambil = search(filename, consumable_history, {'id_pengambil': data[i]["id_pengambil"]})[0]['id_pengambil']
                pengambil = search(filename_user, users, {'id': id_pengambil})[0]['nama']

                id_consumable = search(filename, consumable_history, {'id_consumable': data[i]["id_consumable"]})[0]['id_consumable']
                consumable_yang_diambil = search(filename_consumable, consumable, {'id': id_consumable})[0]['nama']

                print("ID Pengembalian\t\t :", data[i]["id"])
                print("Nama Pengambil\t\t :", pengambil)
                print("Nama Consumable\t\t :", consumable_yang_diambil)
                print("Tanggal Pengambilan\t :", data[i]["tanggal_pengambilan"])
                print("Jumlah\t\t\t :", data[i]["jumlah"])
                print()

            if not last:
                c = input("Apakah Anda ingin melihat riwayat tambahan (y/n)? ")
                idx += 5

def pinjam(userID, gadget, consumable, gadget_borrow_history, folder_name) :
# Fungsi untuk melakukan peminjaman gadget

    data = gadget

    # Menerima input ID
    id = input("Masukan ID item\t\t : ")
    # Memeriksa apakah ID valid atau tidak. Id dikatakan valid jika ID gadget terdapat pada file gadget.csv
    while (id[0] != "G" or mencari_id(id, gadget, consumable, folder_name)[0] == False) : 
        print("ID tidak valid! Periksa kembali ID item")
        id = input("Masukan ID item\t : ")

    # Menerima input tanggal
    tanggal_peminjaman = input("Tanggal Peminjaman (DD/MM/YYYY)\t : ")
    # Memeriksa apakah format tanggal sudah benar
    while (not (is_date_valid(tanggal_peminjaman))) :
        print("Tanggal yang Anda masukkan salah! Format penanggalan adalah DD/MM/YYYY")
        tanggal_peminjaman = input("Tanggal Peminjaman (DD/MM/YYYY)\t : ")
    
    jumlah_peminjaman = int(input("Jumlah Peminjaman\t : "))
    idx_id = mencari_id(id, gadget, consumable, folder_name)[1]  # Indeks pada array data tempat ID gadget berada
    
    # Memeriksa stok gadget berdasarkan ID gadget
    data[idx_id]["jumlah"] = int(data[idx_id]['jumlah'])
    while (data[idx_id]["jumlah"] < jumlah_peminjaman) :
        print("Jumlah peminjaman melebihi stok pada inventori. Kurangi jumlah peminjaman!")
        jumlah_peminjaman = int(input("Jumlah Peminjaman\t : "))
    
    new_data = {'id' : str(get_last_id(gadget_borrow_history) + 1), 'id_peminjam' : userID , 'id_gadget' : id[1], 'tanggal_peminjaman' : tanggal_peminjaman, 'jumlah' : jumlah_peminjaman, 'is_returned' : "False"}
    
    c = input("Apakah Anda yakin ingin meminjam " + data[idx_id]["nama"] + " sebanyak " + str(jumlah_peminjaman) + " buah (y/n)? ")
    if (c in "Yy") :
        if (is_item_returned(userID, id, folder_name) == "False") :
            print("Anda tidak dapat meminjam item yang sama dengan item yang sedang dipinjam")
        else :
            data[idx_id]["jumlah"] -= jumlah_peminjaman
            print("Item " + data[idx_id]['nama'] + "(x" + str(jumlah_peminjaman) + ") berhasil dipinjam!")
            
            return gadget_borrow_history.append(new_data)
    else :
        print("Peminjaman item dibatalkan")
        return None

# gadget borrow testing
# 6;1;6;10/01/2000;1;False

#edge case apa yang terjadi bila id tidak urut 
def kembalikan(userID, gadget_borrow_history, gadget_return_history, gadget, folder_name) :
# Fungsi untuk melakukan pengembalian gadget secara total

    data = gadget_borrow_history
    borrowed_gadget = []    # menyimpan list gadget yang sedang dipinjam
                            # index ganjil menyimpan data gadget yang sedang dipinjam, index genap menyimpan nilai index pada array data dari gadget yang sedang dipinjam

    # Mencari list gadget yang sedang dipinjam oleh user
    for i in range (len(data)) :
        
        if (data[i]["id_peminjam"] == userID and data[i]["is_returned"] == "False") :
            borrowed_gadget.append(i)           # menyimpan nilai index pada array data dari gadget yang sedang dipinjam
            borrowed_gadget.append(data[i])     # menyimpan data gadget yang sedang dipinjam

    if len(borrowed_gadget) == 0 :
        print("Tidak ada gadget yang sedang dipinjam")
        return None, None
    else :
        
        num = 1
        for i in range (1, len(borrowed_gadget), 2) :
            available_gadget = search(folder_name + '/gadget.csv', gadget, {'id': borrowed_gadget[i]["id_gadget"]})[0]['nama']
            print(str(num) + ". " + available_gadget)
            num += 1

        idx_return = int(input("Masukkan nomor peminjaman\t : "))
        idx_return = 2 * idx_return - 1    
        id_gadget = borrowed_gadget[idx_return]["id_gadget"]

        sudah_dikembalikan_sebelumnya = 0

        
        for transaksi in gadget_return_history:
            if transaksi['id_peminjam'] == userID and transaksi['id_gadget'] == id_gadget:
                sudah_dikembalikan_sebelumnya += int(transaksi['jumlah_pengembalian'])

        tanggal_pengembalian = input("Tanggal Pengembalian (DD/MM/YYYY)\t : ")
        # Memeriksa apakah format tanggal sudah benar
        while (not (is_date_valid(tanggal_pengembalian))) :
            print("Tanggal yang Anda masukkan salah! Format penanggalan adalah DD/MM/YYYY")
            tanggal_pengembalian = input("Tanggal Pengembalian (DD/MM/YYYY)\t : ")

        jumlah_dikembalikan = int(input("Banyaknya gadget yang ingin dikembalikan: "))

        if jumlah_dikembalikan + sudah_dikembalikan_sebelumnya == int(borrowed_gadget[idx_return]['jumlah']):
            new_data = {'id' : get_last_id(gadget_return_history) + 1, "id_peminjam" : userID, "id_gadget" : id_gadget , "tanggal_pengembalian" : tanggal_pengembalian, "jumlah_pengembalian": jumlah_dikembalikan}
            for i in range(len(data)):
                if data[i]['id_gadget'] == id_gadget and data[i]['id_peminjam'] == userID:
                    data[i]['is_returned'] = "True"

            print("Item " + search(folder_name + '/gadget.csv', gadget, {'id': id_gadget})[0]['nama'] + "(x" + str(borrowed_gadget[idx_return]['jumlah']) + ") telah dikembalikan sebanyak " + str(jumlah_dikembalikan))
            gadget_return_history.append(new_data)
            return gadget_return_history, data
        elif jumlah_dikembalikan + sudah_dikembalikan_sebelumnya < int(borrowed_gadget[idx_return]['jumlah']):
            new_data = {'id' : get_last_id(gadget_return_history) + 1, "id_peminjam" : userID, "id_gadget" : id_gadget , "tanggal_pengembalian" : tanggal_pengembalian, "jumlah_pengembalian": jumlah_dikembalikan}
            print("Item " + search(folder_name + '/gadget.csv', gadget, {'id': id_gadget})[0]['nama'] + "(x" + str(borrowed_gadget[idx_return]['jumlah']) + ") telah dikembalikan sebanyak " + str(jumlah_dikembalikan))
            gadget_return_history.append(new_data)
            return gadget_return_history , data
        else:
            print("Tidak bisa mengembalikan gadget lebih banyak dari gadget yang dipinjam")
            return None, None
    


def minta(userID, consumable_history, gadget, consumable, folder_name) :
# Fungsi untuk melakukan permintaan consumable

    filename = folder_name + "/consumable.csv"
    data = consumable

    id = input("Masukan ID item\t\t : ")
    # Memeriksa apakah ID item valid atau tidak
    while (id[0] != "C" and mencari_id(id, gadget, consumable, folder_name)[0] == False) :
        print("ID tidak valid! Periksa kembali ID item")
        id = input("Masukan ID item\t : ")

    jumlah_permintaan = int(input("Jumlah \t\t : "))
    idx_id = mencari_id(id, gadget, consumable, folder_name)[1]  # Indeks pada array data tempat ID consumable berada
    # Memeriksa stok consumable berdasarkan ID
    if jumlah_permintaan < 0:
        print("Jumlah consumable yang diminta tidak boleh negatif!")
        return None
    elif jumlah_permintaan > int(data[idx_id]['jumlah']):
        print("Jumlah consumable yang diminta tidak boleh lebih dari stok consumable!")
        return None

    tanggal_pengambilan = input("Tanggal Permintaan (DD/MM/YYYY)\t : ")
    # Memeriksa apakah format tanggal sudah benar
    while (not (is_date_valid(tanggal_pengambilan))) :
        print("Tanggal yang Anda masukkan salah! Format penanggalan adalah DD/MM/YYYY")
        tanggal_pengambilan = input("Tanggal Permintaan (DD/MM/YYYY)\t : ")

    data[idx_id]["jumlah"] = int(data[idx_id]["jumlah"])
    data[idx_id]["jumlah"] -= jumlah_permintaan

    new_data = {'id' : get_last_id(consumable_history) + 1, 'id_pengambil' : userID , 'id_consumable' : id[1], 'tanggal_pengambilan' : tanggal_pengambilan, 'jumlah' : jumlah_permintaan}
    
    consumable_history.append(new_data)

    print("Item " + data[idx_id]['nama'] + "(x" + str(jumlah_permintaan) + ") telah berhasil diambil!")
    return consumable_history




# riwayatpinjam()
# riwayatkembali()
# riwayatambil()
# print(search_user_by_id("2"))
# print(is_date_valid("01/02/1990"))
