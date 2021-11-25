def split_csv(string, delimiters=";\n"):
    result = []
    word = ""
    for i in string:
        if i not in delimiters:
            word += i
        elif word:
            result.append(word)
            word = ""
    if word:
        result.append(word)
    return result


def search_by_rarity(filename):
    with open(filename, "r") as data:
        print(">>> mencari berdasarkan rarity")
        rarity_input = input("Masukkan rarity : ")
        length = 0
        results = []

        count = 0
        for line in data:
            words = split_csv(line)
            results.append((words[0:]))
            length += 1

        
        for i in range(0, length):
            if results[i][4] == rarity_input:
                print(results[i])
                count = count +1
        if (count == 0):
            print("ID tidak ditemukan")

def search_by_year(filename):
    with open(filename, "r") as data:
        print(">>> mencari berdasarkan tahun ditemukan")
        year_input = int(input("Masukkan tahun : "))
        kategori = input("masukkan kategori : ")
        length = 0
        results = []

        count = 0
        
        for line in data:
            words = split_csv(line)
            results.append((words[0:]))
            length += 1


        for i in range(0, length):
            if (kategori == ("=")):
                if (results[i][5] == year_input):
                    print(results[i])
                    count = count + 1
                else:
                    continue
            elif (kategori == (">")):
                if (results[i][5] > year_input):
                    print(results[i])
                    count = count + 1
                else:
                    continue
            elif (kategori == ("<")):
                if (results[i][5] < year_input):
                    print(results[i])
                    count = count + 1
                else:
                    continue
            elif (kategori == (">=")):
                if (results[i][5] >= year_input):
                    print(results[i])
                    count = count + 1
                else:
                    continue
            elif (kategori == ("<=")):
                if (results[i][5] <= year_input):
                    print(results[i])
                    count = count + 1
                else:
                    continue
            else:
                continue
        if (count == 0):
            print("tidak ada data yang ditemukan")
                


def update_data(filename):
    with open(filename, "w") as data:
        print(">>> update data berdasarkan ID")
        id_input = input("Masukkan ID : ")
        length = 0
        results = []

        count = 0
        for line in data:
            words = split_csv(line)
            results.append((words[0:]))
            length += 1
        for i in range(0, length):
            if results[i][0] == id_input:
                for j in range(len(results[i])):
                    results[i][j]= input()

                    count = count + 1
            else:
                continue
        if (count == 0):
            print("tidak ada data yang ditemukan")
