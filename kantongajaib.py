from autentikasi import *
from gadget import *
from utility import *

# untuk authorization
akses = {
    'akun': None,
    "user": False,
    "admin": False
}

# folder_name merupakan nama_folder pada F14
consumable, consumable_history, gadget, gadget_borrow_history, gadget_return_history, users, folder_name = load_data()

if __name__ == '__main__':
    finish = False
    perubahan = False
    if folder_name != None:
        
        akses = login(users)
        print()
        print()
        print("Berikut perintah yang dapat tersedia:\n")
        
        help()

        print()
        print()

        
    while not finish:
        if folder_name == None:
            # folder tidak ada
            finish = True
            continue
        
        
        perintah = input('>>> ')
        # khusus untuk prosedur register akan save data secara otomatis
        if perintah == 'register':
            if akses['admin'] == True:
                users = register(users)
                perubahan = True
            else:
                print("Anda bukan Admin")

        elif perintah == 'carirarity':
            carirarity(folder_name, gadget)

        elif perintah == 'caritahun':
            caritahun(folder_name, gadget)

        elif perintah == 'tambahitem':
            if akses['admin'] == False:
                print("Anda bukan admin")
                continue
            jenis, data = tambahitem(folder_name, gadget, consumable)
            if jenis == 'gadget':
                gadget = (data)
            elif jenis == 'consumable':
                consumable = (data)

            perubahan = True

        elif perintah == 'hapusitem':
            if akses['admin'] == False:
                print("Anda bukan admin")
                continue
            jenis, data = hapusitem(folder_name, gadget, consumable)
            if jenis == 'gadget':
                gadget = (data)
            elif jenis == 'consumable':
                consumable = (data)

            print("Item berhasil dihapus")

            perubahan = True

        elif perintah == 'ubahjumlah':
            if akses['admin'] == False:
                print("Anda bukan admin")
                continue
            jenis, data = ubahjumlah(folder_name, gadget, consumable)
            if jenis == 'gadget':
                gadget = (data)
            elif jenis == 'consumable':
                consumable = (data)

            perubahan = True

        elif perintah == 'pinjam':
            if akses['user'] == False:
                print("Hanya user yang boleh meminjam")
                continue
            ret = pinjam(akses['akun']['id'], gadget, consumable, gadget_borrow_history, folder_name)
            if ret != None:
                gadget_borrow_history = (ret)
                perubahan =  True

        elif perintah == 'kembalikan':
            if akses['user'] == False:
                print("Hanya user yang boleh mengembalikan")
                continue
            ret, update = kembalikan(akses['akun']['id'], gadget_borrow_history, gadget_return_history, gadget, folder_name)
            if ret != None:
                
                gadget_return_history = (ret)
                gadget_borrow_history = (update)

                print(gadget_return_history)
                perubahan = True

        elif perintah == 'minta':
            if akses['user'] == False:
                print("Hanya user yang boleh meminta consumable")
                continue
            
            ret = minta(akses['akun']['id'], consumable_history, gadget, consumable, folder_name)

            if ret != None:
                consumable_history = ret
                perubahan = True

        elif perintah == 'riwayatpinjam':
            if akses['admin'] == False:
                print("Anda bukan admin")
                continue
            riwayatpinjam(folder_name, gadget_borrow_history, gadget, users)

        elif perintah == 'riwayatkembali':
            if akses['admin'] == False:
                print("Anda bukan admin")
                continue
            riwayatkembali(folder_name, gadget_return_history, gadget, users)

        elif perintah == 'riwayatambil':
            if akses['admin'] == False:
                print("Anda bukan admin")
                continue

            riwayatambil(folder_name, consumable_history, consumable, users)

        elif perintah == 'help':
            help()

        elif perintah == 'exit':
            if perubahan == True:
                keluar(consumable, consumable_history, gadget, gadget_borrow_history, gadget_return_history, users, folder_name)
            else:
                print("Tidak ada perubahan yang dilakukan")
            finish = True

        elif perintah == 'save':
            save(consumable, consumable_history, gadget, gadget_borrow_history, gadget_return_history, users, folder_name)

        

        

        
    print("Program selesai")



