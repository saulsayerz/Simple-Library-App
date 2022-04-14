import argparse
import os
from datetime import datetime
#jika file .csv kosong, buat baru, isi baris 1 dengan headernya
def isi_kosong(file_path):
    nama_csv = [
        'consumable.csv', 
        'consumable_history.csv', 
        'gadget.csv', 
        'gadget_borrow_history.csv',
        'gadget_return_history.csv',
        'user.csv',
    ]

    header_csv = [
        'id;nama;deskripsi;jumlah;rarity',
        'id;id_pengambil;id_consumable;tanggal_peminjaman;jumlah',
        'id;nama;deskripsi;jumlah;rarity;tahun_ditemukan',
        'id;id_peminjam;id_gadget;tanggal_peminjaman;jumlah',
        'id;id_peminjam;id_gadget;tanggal_pengembalian',
        'id;username;nama;alamat;password;role'
    ]

    for i in range(len(nama_csv)):
        if not os.path.isfile(file_path + '/' + nama_csv[i]):
            with open(file_path + '/' + nama_csv[i], 'w') as tulis:
                tulis.writelines(header_csv[i])


def get_consumable_history(folder_name):
    remove_all_empty_lines(folder_name + '/consumable_history.csv')
    return get_all_to_dictionary(folder_name + '/consumable_history.csv')

def get_consumable(folder_name):
    remove_all_empty_lines(folder_name + '/consumable.csv')
    return get_all_to_dictionary(folder_name + '/consumable.csv')

def get_gadget_borrow_history(folder_name):
    remove_all_empty_lines(folder_name + '/gadget_borrow_history.csv')
    return get_all_to_dictionary(folder_name + '/gadget_borrow_history.csv')

def get_gadget_return_history(folder_name):
    remove_all_empty_lines(folder_name + '/gadget_return_history.csv')
    return get_all_to_dictionary(folder_name + '/gadget_return_history.csv')

def get_gadget(folder_name):
    remove_all_empty_lines(folder_name + '/gadget.csv')
    return get_all_to_dictionary(folder_name + '/gadget.csv')

def get_users(folder_name):
    remove_all_empty_lines(folder_name + '/user.csv')
    return get_all_to_dictionary(folder_name + '/user.csv')


# mengembalikan folder_name yg di parsing di commandline
def get_folder_name():
    program_parser = argparse.ArgumentParser(prog="Kantong Ajaib Doremonangis",
                                          usage="python kantongajaib.py <folder_name>",
                                          description="Silahkan masukkan nama folder lokasi file-file csv")

    program_parser.add_argument("folder_name")
    args = program_parser.parse_args()

    file_path = args.folder_name

    return file_path
    
def load_data():
    folder_name = get_folder_name()
    
    if not os.path.isdir(folder_name):
        print("Folder tidak ditemukan!")
        return None, None, None, None, None, None, None
    else:
        isi_kosong(folder_name)
        return get_consumable(folder_name), get_consumable_history(folder_name), get_gadget(folder_name), get_gadget_borrow_history(folder_name), get_gadget_return_history(folder_name), get_users(folder_name), folder_name


# urutan
# data\consumable.csv
# data\consumable_history.csv
# data\gadget.csv
# data\gadget_borrow_history.csv
# data\gadget_return_history.csv
# data\user.csv
        

# isi consumable_history: 5;12321313;390;DD/MM/YEYE;1238

def split_csv(string, delimiter=';'):
    result = []
    data = ''

    for letter in string:
        if letter not in delimiter:
            data += letter

        else:
            if data != '':
                result.append(data)
                data = ''

    if data != '':
        result.append(data)

    return result


# header dari file
# header disimpan dalam bentuk array
# lihat test.py untuk penggunaan
def get_header(filename):    
    with open(filename, 'r') as file_data:
        head_data = file_data.readlines()[0]
        head_data = split_csv(head_data)

        head_data = remove_if_last_enter(head_data)
        return head_data


# data berupa dictionary misal {"id": 1, "nama": "anonim", ...}
def is_format_correct(data, filename):
    head = get_header(filename)
    
    inputan = [*data]

    for i in range(len(inputan)):
        if head[i] != inputan[i]:
            return False

    return True


# membuat data, cara menambahkan data ada di test.py
def create(data, filename):
    remove_all_empty_lines(filename)
    string = ''
    
    # jika data yang ingin dimasukkan ke dalam file tidak memiliki id
    # tambahkan id dengan mengambil id terbesar
    # if data.get('id') == None:
    #     temp_id = {
    #         "id": get_last_id(filename)+1
    #     }
    #     data = {**temp_id, **data}
    
    # error handling
    if not is_format_correct(data, filename):
        correct_header = get_header(filename)
        raise Exception(f"Header harus: {correct_header}")

    list_key = [*data]

    for key in list_key:
        string += str(data[key])
        string += ';'

    string = remove_last_char(string)
    a = ''

    with open(filename, 'r') as user_file:
        a = user_file.read()
    
    if list(a[-1]) != '\n':
        with open(filename, 'a') as user_file:
            user_file.write('\n')
    
    with open(filename, 'a') as user_file:
        user_file.write(string)

    remove_all_empty_lines(filename)

# mengemblaikan array of dictionary tiap record/data pada csv
def get_all_to_dictionary(filename):
    
    arr = get_all_data(filename)

    head = get_header(filename)
    clean = []
    return_data = []    

    for data in arr:
        clean.append(split_csv(data))

    for i in clean:
        temp = {}
        
        for j in range(len(head)):
            temp[head[j]] = i[j]

        return_data.append(temp)

    return return_data


# mengembalikan id terbesar (dalam integer) pada array of dictionary
def get_last_id(arr):

    # data kosong
    if arr == []:
        return 0
    
    after_sorted = sort_by_key(arr, 'id')
    last_element = after_sorted[-1]
    
    return int(last_element['id'])

# sort ascending by key, key harus integer
def sort_by_key(arr, key):
    newlist = sorted(arr, key=lambda k: int(k[key])) 
    return newlist

# mungkin akan dihapus
# dari dictionary ke string csv
# contoh query = {"nama": "saya", "pelajaran": "fisika"}
# akan mengembalikan 'saya;pelajaran\n'
# perhatikan bahwa ada enter di ujung
# dictionary harus lengkap mengikuti format header
# bila namun, bila id tidak diberikan, id akan ditambahkan secara default dengan get_last_id + 1
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



def remove_if_last_enter(arr):
    last_member = arr[len(arr)-1]
    if last_member[len(last_member)-1] == '\n':
        arr[len(arr)-1] = last_member[:len(last_member)-1]

    return arr

def remove_last_char(string):
    return string[:len(string)-1]

# mengembalikan array yang masing masing elemennya merupakan string pada tiap baris di file
def get_all_data(filename):
    
    with open(filename, 'r') as f:
        read_line = f.readlines()

    arr = []
    for line in read_line:
        arr.append(''.join(remove_if_last_enter(list(line))))
    
    return arr[1:]
                    
# merapikan data dengan menghapus semua baris kosong
def remove_all_empty_lines(filename):
    arr = get_all_data(filename)

    counter = 0

    head = ''
    with open(filename, 'r') as data:
        head = data.readlines()[0]

    with open(filename, 'w') as data:

        data.write(head)
        for i in arr:
            if list(i) != []:
                data.write(i)
                data.write('\n')

# mengembalikan array of dictionary dari suatu file
def get_data(filename):
    folder_name, file_name = split_csv(filename, '/')

    if file_name == 'gadget.csv':
        return get_gadget(folder_name)
    elif file_name == 'consumable.csv':
        return get_consumable(folder_name)
    elif file_name == 'consumable_history.csv':
        return get_consumable_history(folder_name)
    elif file_name == 'gadget_borrow_history.csv':
        return get_gadget_borrow_history(folder_name)
    elif file_name == 'gadget_return_history.csv':
        return get_gadget_return_history(folder_name)
    elif file_name == 'user.csv':
        return get_users(folder_name)
    else:
        return []

#CONTOH APLIKASI SEARCH(filename,cari) :
#print(search('data/gadget.csv', {"rarity" : "SSS"}))

def search(filename, data, cari) :
    head = get_header(filename)
    ada = False
    kategori = [*cari][0]
    nama = cari[kategori]
    for i in range (len(head)) :        #VALIDISASI APAKAH KATEGORI YANG DIINPUT ADA DI FILENAME
        if head[i] == [kategori][0] :
            indeks = i
            ada = True
    if ada == False : 
        print("Kategori yang ingin dicari tidak ada dalam file")  # Apabila kategori tidak ada dalam filename
        return
    else : 
        bersih = []
        kotor = data 
        for i in range (len(kotor)) :
            if kotor[i][kategori] == nama :
                bersih.append(kotor[i])
        return bersih

def bulk_write(data, from_folder, to_folder, csv_name, belum_ada, header):
    os.chdir(to_folder)
    if os.name == 'nt':
        os.system("cd . > " + csv_name)
    else:
        os.system("touch " + csv_name)
    
    os.chdir('..')
    with open(to_folder + '/' + csv_name, 'w') as f:
        head = split_csv(header)
        string = ''
        for i in head:
            string += i + ';'

        string = string[:len(string)-1]
        f.writelines(string)
    for i in data:
        create(i, to_folder +'/' + csv_name)


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


def is_item_returned(idUser, idGadget, folder_name) :
# Memeriksa apakah user sedang meminjam gadget yang sama atau tidak
# Mengembalikan true jika user sedang meminjam gadget yang sama

    filename = folder_name + "/gadget_borrow_history.csv"
    data = get_data(filename)

    isReturned = True
    i = 0

    while (i < len(data) and isReturned == True) :
        if (idUser == data[i]["id_peminjam"]) :
            if (idGadget == data[i]['id_gadget'] and data[i]["is_returned"] == "True") :
                i += 1
            else : 
                isReturned = False
        else :
            i += 1

    return isReturned

# INI ITU FUNGSI UNTUK MENCARI ID APAKAH ADA ATAU TIDAK
# HASIL FUNGSINYA ITU MERETURN SEBUAH TUPLE, ISINYA (True/False , id ditemukan di urutan berapa)          
def mencari_id(ID, gadget, consumable, folder_name) :
    id_ada = False # Untuk mengecek apakah ID sudah ada atau tidak
    urutan_id = -1
    if ID[0] == 'G' :
        datagadget = gadget
        for i in range (len(datagadget)) : # Mengecek apakah id ada di data gadget
            if ID[1:] == datagadget[i]['id'] :
                id_ada = True
                urutan_id = i
                break
    if ID[0] == 'C' :
        datac = consumable
        for i in range (len(datac)) : # Mengecek apakah id ada di data consumable
            if ID[1:] == datac[i]['id'] :
                id_ada = True
                urutan_id = i
                break
    return id_ada, urutan_id

# deep copy dua array
def deep_copy(arr1):
    temp = []
    panjang = len(arr1)
    for i in range(panjang):
        temp.append(arr1[i])

    return temp