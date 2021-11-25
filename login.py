from utility import *

def login(filename):
    with open(filename, "r") as data:
        print(">>> login")
        username_input = input("Masukkan username : ")
        password_input = input("Masukkan password : ")
        
        results = get_all_data(filename)

        length = len(results)
        
        for data in results:
            clean_data = split_csv(data)
            if clean_data[1] == username_input and clean_data[4] == password_input:
                print("Selamat datang {}!".format(username_input))
                
                if clean_data[5] == 'Admin':
                    register(filename)
                else:
                    print("Karena aplikasi belum selesai dan Anda bukan admin, anda akan dipaksa keluar")

                return


        print("Credentials anda salah. Silahkan coba lagi")
        login(filename)


def register(filename):
    with open(filename, "r") as data:
        length = 0
        current_data = []
        for line in data:
            words = split_csv(line)
            current_data.append((words[0:]))
            length += 1
            
    with open(filename, "a") as data:
        upload_data = ""
        print(">>> register")
        new_name = str.title(input("Masukkan nama : "))
        new_username = input("Masukkan username : ")
        for i in range(0, length):
            if current_data[i][1] == new_username:
                print("Username exists. Please use another one!")
                register(filename)
        
        new_password = input("Masukkan password : ")
        new_address = input("Masukkan alamat : ")
        new_id = str(get_last_id(filename)+1)
        upload_data = (new_id + ";" + new_username + ";" + new_name + ";" + new_address + ";" + new_password + ";" + "User")
        print("User {} telah berhasil register ke dalam Kantong Ajaib".format(new_username))
        data.write("\n")
        data.write(upload_data)

