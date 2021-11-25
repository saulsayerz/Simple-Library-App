from .helper import split_csv, remove_if_last_enter, remove_last_char

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
    if data.get('id') == None:
        temp_id = {
            "id": get_last_id(filename)+1
        }
        data = {**temp_id, **data}
    
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

# sort ascending by key, key harus integer
def sort_by_key(arr, key):
    newlist = sorted(arr, key=lambda k: int(k[key])) 
    return newlist

# mengurutkan data yang ada di csv by key
def sort_csv_by_key(filename, key):
    arr = get_all_to_dictionary(filename)
    
    after_sorted = sort_by_key(arr, key)

    first_data = ''

    with open(filename, 'r') as f:
        first_data = f.readlines()[0]
    
    with open(filename, 'w') as f:    
        f.writelines(first_data)
    
    for i in after_sorted:
        create(i, filename)

    remove_all_empty_lines(filename)

# mengembalikan id terbesar (dalam integer) pada array of dictionary
def get_last_id(filename):
    arr = get_all_to_dictionary(filename)
    
    after_sorted = sort_by_key(arr, 'id')
    last_element = after_sorted[-1]
    
    return int(last_element['id'])


