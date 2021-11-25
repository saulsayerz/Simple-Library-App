# from utility import *


# user_dummy = {
#     #"id": '20',
#     "username": 'bebas',
#     "nama": "my name is",
#     "alamat": "Jl. Ganesha",
#     "password": "Mau tau aja",
#     "role": "ngadimin"
# }

# gadget_dummy = {
#     "id": "2",
#     "nama": "Bukan Windows",
#     "deskripsi": "Turunan ARM",
#     "jumlah": 10,
#     "rarity": "S",
#     "tahun_ditemukan": "1945"
# }

# consumable_dummy = {
#     "id": 9,
#     "nama": "mangsut?",
#     "deskripsi": "ini berguna",
#     "jumlah": "4",
#     "rarity": "C"
# }

# consumable_history_dummy = {
#     "id": 5,
#     "id_pengambil": 12321313,
#     "id_consumable": 390,
#     "tanggal_peminjaman": "DD/MM/YEYE",
#     "jumlah": 1238

# }

# gadget_borrow_history = {
#     "id": 5,
#     "id_peminjam": 12321313,
#     "id_gadget": 390,
#     "tanggal_peminjaman": "DD/MM/YEYE",
#     "jumlah": 1238
# }


# gadget_return_history = {
#     "id": 5,
#     "id_peminjam": 12321313,
#     "id_gadget": 390,
#     "tanggal_pengembalian": "DD/MM/YEYE",
# }

# filename = 'data/users.csv'
# create(user_dummy, filename)
# head = get_header(filename)
# print(f"header dari {filename} adalah {head}")
# print(f"Data {user_dummy} telah dimasukkan ke dalam {filename}")

# filename2 = 'data/gadget.csv'
# create(gadget_dummy, filename2)
# head2 = get_header(filename2)
# print(f"header dari {filename2} adalah {head2}")
# print(f"Data {gadget_dummy} telah dimasukkan ke dalam {filename2}")

# filename3 = 'data/consumable.csv'
# create(consumable_dummy, filename3)
# head3 = get_header(filename3)
# print(f"header dari {filename3} adalah {head3}")
# print(f"Data {consumable_dummy} telah dimasukkan ke dalam {filename3}")

# filename4 = 'data/consumable_history.csv'
# create(consumable_history_dummy, filename4)
# head4 = get_header(filename4)
# print(f"header dari {filename4} adalah {head4}")
# print(f"Data {consumable_history_dummy} telah dimasukkan ke dalam {filename4}")

# filename5 = 'data/gadget_borrow_history.csv'
# create(gadget_borrow_history, filename5)
# head5 = get_header(filename5)
# print(f"header dari {filename5} adalah {head5}")
# print(f"Data {gadget_borrow_history} telah dimasukkan ke dalam {filename5}")

# filename6 = 'data/gadget_return_history.csv'
# create(gadget_return_history, filename6)
# head6 = get_header(filename6)
# print(f"header dari {filename6} adalah {head6}")
# print(f"Data {gadget_return_history} telah dimasukkan ke dalam {filename6}")

# # merapikan data dengan menghapus semua baris kosong
# remove_all_empty_lines(filename)
# remove_all_empty_lines(filename2)
# remove_all_empty_lines(filename3)
# remove_all_empty_lines(filename4)
# remove_all_empty_lines(filename5)
# remove_all_empty_lines(filename6)

# all_data = get_all_data(filename2)
# print(all_data)

# arr = get_all_to_dictionary(filename)

# sort_csv_by_key(filename, 'id')
# sort_csv_by_key(filename2, 'id')

# string = dict_to_csv(filename, arr[0])
# ada enter di ujung jadi tinggal di insert aja
# print(list(string))

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

def get_data(folder_name, csv_name):
    pass


def search(filename, cari) :
    # head = get_header(filename)
    ada = False
    kategori = [*cari][0]
    nama = cari[kategori]
    csv_name = split_csv(filename '/')[1]
    
    a = get_data(csv_name)

    for i in range (len(head)) :        #VALIDISASI APAKAH KATEGORI YANG DIINPUT ADA DI FILENAME
        if head[i] == [kategori][0] :
            indeks = i
            ada = True
    if ada == False : 
        print("Kategori yang ingin dicari tidak ada dalam file")  # Apabila kategori tidak ada dalam filename
        return
    else : 
        bersih = []
        folder_name, csv_name = split_csv(filename)
        kotor = get_data(folder_name, csv_name)
        # kotor = get_all_to_dictionary(filename) #Apabila kategori ada, dan mencari hal yang diinginkan di kategori
        for i in range (len(kotor)) :
            if kotor[i][kategori] == nama :
                bersih.append(kotor[i])
        return bersih

cari = {'username': 'lolxd'}
search('data/users.csv', cari)