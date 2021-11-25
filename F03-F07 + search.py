from utility import *

def search(filename, cari) :
    head = get_header(filename)
    ada = False
    kategori = [*cari][0]
    nama = cari[kategori]
    print(nama,kategori)
    for i in range (len(head)) :        #VALIDISASI APAKAH KATEGORI YANG DIINPUT ADA DI FILENAME
        if head[i] == [kategori][0] :
            indeks = i
            ada = True
    if ada == False : 
        print("Kategori yang ingin dicari tidak ada dalam file")  # Apabila kategori tidak ada dalam filename
        return
    else : 
        bersih = []
        kotor = get_all_to_dictionary(filename) #Apabila kategori ada, dan mencari hal yang diinginkan di kategori
        for i in range (len(kotor)) :
            if kotor[i][kategori] == nama :
                bersih.append(kotor[i])
        return bersih
#CONTOH APLIKASI SEARCH(filename,cari) :
#print(search('data/gadget.csv', {"rarity" : "SSS"}))

def carirarity() :
    rarity = input("Masukkan rarity: ")
    cari = {"rarity" : rarity}
    clean = search('temporary/gadget.csv', cari) #memanfaatkan fungsi yang sudah ada
    for i in range (len(clean)) : # Untuk mencetak tiap data dari data clean yang berarti ada rarity yang diminta
        print("Nama            :", clean[i]["nama"])
        print("Deskripsi       :", clean[i]["deskripsi"])
        print("Jumlah          :", clean[i]["jumlah"])
        print("Rarity          :", clean[i]["rarity"])
        print("Tahun Ditemukan :", clean[i]["tahun_ditemukan"])
    return
#carirarity()

def caritahun() :
    tahun = int(input("Masukkan tahun: "))
    kategori = input("Masukkan kategori: ")
    print("\n Hasil pencarian: \n")
    bersih = []
    kotor = get_all_to_dictionary('temporary/gadget.csv') #Apabila kategori ada, dan mencari hal yang diinginkan di kategori
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
    if len(bersih) == 0:
        print('Tidak ada data ditemukan')
    return
#CONTOH APLIKASI caritahun(filename) :
#caritahun('data/gadget.csv')

# INI ITU FUNGSI UNTUK MENCARI ID APAKAH ADA ATAU TIDAK
# HASIL FUNGSINYA ITU MERETURN SEBUAH TUPLE, ISINYA (True/False , id ditemukan di urutan berapa)          
def mencari_id(ID) :
    id_ada = False # Untuk mengecek apakah ID sudah ada atau tidak
    urutan_id = -1
    if ID[0] == 'G' :
        datagadget = get_all_to_dictionary('temporary/gadget.csv')
        for i in range (len(datagadget)) : # Mengecek apakah id ada di data gadget
            if ID[1:] == datagadget[i]['id'] :
                id_ada = True
                urutan_id = i
                break
    if ID[0] == 'C' :
        datac = get_all_to_dictionary('temporary/consumable.csv')
        for i in range (len(datac)) : # Mengecek apakah id ada di data consumable
            if ID[1:] == datac[i]['id'] :
                id_ada = True
                urutan_id = i
                break
    return id_ada, urutan_id

def tambahitem() :
    ID = input("Masukan ID: ")
    if (ID[0] != 'G' and ID[0] != 'C') : # Untuk mengecek apakah ID sudah sesuai format atau tidak
        print("Gagal menambahkan item karena ID tidak valid.") 
        return
    else :
        id_ada= mencari_id(ID)[0] #Mencari ID apakah ada atau tidak dengan fungsi yang sudah dibuat
        if id_ada == True :
            print("Gagal menambahkan item karena ID sudah ada.") # Mencetak demikian apabila data sudah ada
        else :
            nama = input("Masukan Nama: ")
            deskripsi = input("Masukan Deskripsi: ")
            jumlah = int(input("Masukan Jumlah: "))
            if jumlah < 0 :
                print("input jumlah tidak valid!") #Karena jumlah stok tidak bisa negatif
                return
            rarity = input("Masukan Rarity: ")
            if rarity != 'C' and rarity != 'B' and rarity != 'A' and rarity !='S' : 
                print("input rarity tidak valid!") # Untuk rarity yang tidak valid
                return
            if ID[0] == 'G' : # Untuk kasus ID adalah gadget
                tahun = input("Masukan tahun ditemukan: ") #asumsi tahun negatif = sebelum masehi
                data_baru = {'id': ID[1:], 'nama': nama, 'deskripsi': deskripsi, 'jumlah': str(jumlah), 'rarity': rarity, 'tahun_ditemukan': tahun}
                create(data_baru,'temporary/gadget.csv')
                sort_csv_by_key('temporary/gadget.csv', 'id')
            else : # Untuk kasus ID adalah consumable
                data_baru = {'id': ID[1:], 'nama': nama, 'deskripsi': deskripsi, 'jumlah': str(jumlah), 'rarity': rarity}
                create(data_baru,'temporary/consumable.csv')
                sort_csv_by_key('temporary/consumable.csv', 'id')
            print("Item telah berhasil ditambahkan ke database")
            return
#tambahitem()

        
def dict_to_csv(filename, query):
    head = get_header(filename)
    string = ''

    if query.get('id') == None:
        query['id'] = get_last_id(filename) + 1

    string += query['id']

    for head_data in head[1:]:
        string += ';' + query[head_data]

    string += '\n'

    return string


def ubahjumlah() :
    ID = input("Masukan ID: ")
    id_ada = mencari_id(ID)[0] # Mengecek apakah ID ada atau tidak menggunakan fungsi yang sudah ada
    if id_ada == False or (ID[0] != 'G' and ID[0] != 'C') :
        print("Tidak ada item dengan ID tersebut!")
        return
    else : # Untuk kasus bahwa ID ada
        urutanID = mencari_id(ID)[1]
        if ID[0] == 'G' : #Untuk mencari di data Gadget
            data = get_all_to_dictionary('temporary/gadget.csv')
            stok_awal = data[urutanID]['jumlah']
        else : #Untuk mencari data di consumable
            data = get_all_to_dictionary('temporary/consumable.csv')
            stok_awal = data[urutanID]['jumlah']
        jumlah = int(input("Masukan Jumlah: "))
        if int(stok_awal) + jumlah < 0 : # Apabila stoknya menjadi negatif karena kebuang terlalu banyak
            print(jumlah, data[urutanID]['nama'], 'Gagal dibuang karena stok kurang. Stok sekarang:', stok_awal, "(<", str(jumlah*-1) + ")")
        else : #Untuk kasus stoknya tetap valid
            data[urutanID]['jumlah'] = str(int(stok_awal) + jumlah)
            if ID[0] == 'G' : 
                with open('temporary/gadget.csv', 'r') as user_file: 
                    head = user_file.readline()
                lines = []
                for i in range (len(data)) :
                    lines += [dict_to_csv('temporary/gadget.csv',data[i])]
                with open('temporary/gadget.csv', 'w') as user_file: #Untuk menuliskan data yang baru ke CSV gadget
                    user_file.write(head)
                    for i in range (len(data)) :
                        user_file.write(lines[i])
            else :
                with open('temporary/consumable.csv', 'r') as user_file: 
                    head = user_file.readline()
                lines = []
                for i in range (len(data)) :
                    lines += [dict_to_csv('temporary/consumable.csv',data[i])]
                with open('temporary/consumable.csv', 'w') as user_file: #Untuk menuliskan data yang baru ke CSV consumable
                    user_file.write(head)
                    for i in range (len(data)) :
                        user_file.write(lines[i])
            print(jumlah, data[urutanID]['nama'], "berhasil ditambahkan. Stok sekarang:", str(int(stok_awal)+jumlah))
#ubahjumlah()
    
def hapusitem() :
    ID = input("Masukan ID item: ")
    id_ada = mencari_id(ID)[0] # Mengecek apakah ID ada atau tidak menggunakan fungsi yang sudah ada
    if id_ada == False or (ID[0] != 'G' and ID[0] != 'C') :
        print("Tidak ada item dengan ID tersebut!")
        return
    else : # Untuk kasus itemnya ada
        urutan_id = mencari_id(ID)[1]
        if ID[0] =='G' : # Mengambil data gadget
            data = get_all_to_dictionary('temporary/gadget.csv')
        else : # Mengambil data consumable
            data = get_all_to_dictionary('temporary/consumable.csv')
        yakin = input("Apakah anda yakin ingin menghapus " + data[urutan_id]['nama']+ " (Y/N)? ")
        if yakin == "Y" : #Apabila memilih yakin
            data.pop(urutan_id)
            if ID[0] == 'G' : 
                with open('temporary/gadget.csv', 'r') as user_file: 
                    head = user_file.readline()
                lines = []
                for i in range (len(data)) :
                    lines += [dict_to_csv('temporary/gadget.csv',data[i])]
                with open('temporary/gadget.csv', 'w') as user_file: #Untuk menuliskan data yang baru ke CSV gadget
                    user_file.write(head)
                    for i in range (len(data)) :
                        user_file.write(lines[i])
            else :
                with open('temporary/consumable.csv', 'r') as user_file: 
                    head = user_file.readline()
                lines = []
                for i in range (len(data)) :
                    lines += [dict_to_csv('temporary/consumable.csv',data[i])]
                with open('temporary/consumable.csv', 'w') as user_file: #Untuk menuliskan data yang baru ke CSV consumable
                    user_file.write(head)
                    for i in range (len(data)) :
                        user_file.write(lines[i])
            print("Item telah berhasil dihapus dari database.")
        else : #Apabila memilih tidak yakin untuk dibatalkan
            print("Penghapusan item dibatalkan.")
#hapusitem()
    
def pinjam(stat, name): #Ini yang buat gede 
    status = stat
    id_borrower = name
    check_id = str.title(input("Masukkan ID item : "))
    borrowed_data = []
    with open("gadget.csv", "r") as data:
        length = 0
        current_data = []
        for line in data:
            words = split_csv(line)
            current_data.append((words[0:]))
            length += 1
    state = False
    selected_data = []
    for i in range(0, length):
        if current_data[i][0] == check_id:
            state = True
            selected_data = current_data[i]
    if state:
        borrow_date = input("Tanggal peminjaman dalam format dd/mm/yyyy : ")
        check_date = borrow_date.lower()
        if not(check_date.islower()):
            borrow_qty = int("Jumlah peminjaman : ")
            if borrow_qty <= selected_data[3]:
                borrowed_data_str = "B" + ";" + id_borrower + ";" + check_id + ";" + check_date + ";" + borrow_qty + "FALSE"
                borrowed_data.append(borrowed_data_str)
            else:
                print("Jumlah gadget yang ingin dipinjam melebihi stok gadget")
    else:
        print("ID tidak ditemukan. Silahkan input ulang datanya")
        
#print(get_header('data/gadget.csv'))
):


    
    
        
        
        
        
        
    
    
    