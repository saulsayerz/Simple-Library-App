from utility import *

# File ini merupakan semua fungsi utama pada F01 dan F02 dan bonus FB01

def login(users):
    akses = {
        "user": False,
        "admin": False
    }

    while True:
        username_input = input("Masukkan username : ")
        password_input = hash_pass(input("Masukkan password : "))
        
        #corner case: apa yg terjadi bila user.csv kosong ?
        for data in users:
            if data['username'] == username_input and data['password'] == password_input:
                print('Halo ' + username_input + '! Selamat datang di Kantong Ajaib')

                if data['role'] == 'Admin':
                    akses['admin'] = True
                else:
                    akses['user'] = True

                akses['akun'] = data
                return akses

        print("Credentials anda salah. Silahkan coba lagi")
    


def register(users):
    all_user = users

    length = len(all_user)

    new_name = ''
    new_username = ''

    username_exist = True
    while username_exist:
        
        new_name = str.title(input("Masukkan nama : "))
        new_username = input("Masukkan username : ")
        for user in all_user:
            if user['username'] == new_username:
                print("Username telah ada, pilih username lain")
                continue

        username_exist = False

        


    new_password = hash_pass(input("Masukkan password : "))
    new_address = input("Masukkan alamat : ")
    
    
    sort_users = sort_by_key(users, 'id')
    last_element = sort_users[-1]
    new_id = int(last_element['id']) + 1

    
    user = {
        'id': new_id,
        'username': new_username,
        'nama': new_name,
        'alamat': new_address,
        'password': new_password,
        'role': 'User'
    }

    print("User {} telah berhasil register ke dalam Kantong Ajaib!".format(new_username))


    users.append(user)
    
    return users


