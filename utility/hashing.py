def hash_pass(string):
    # inisiasi variabel byte untuk menyimpan byte dari teks password yang dimasukkab
    byte = ""

    # Agar hasil hashing tetap sama, maka digunakan header konstan berikut ini yang
    # diambil dari header hashing MD4 dan MD5.
    h0 = 0x67452301
    h1 = 0xEFCDAB89
    h2 = 0x98BADCFE

    # Variabel byte menyimpan setiap byte dari unicode setiap karakter pada string
    for n in range(len(string)):
        byte += '{0:08b}'.format(ord(string[n]))
    bits = byte + "1"
    # Padding (diadaptasi dari hashing MD5) adalah proses untuk memastikan
    # panjang text dalam bit adalah 448. Proses padding melibatkan append "0"
    # ke dalam bits hingga panjangnya 448. Setelah itu, text sepanjang 448 bit itu
    # ditambahkan text asli sepanjang 64 sehingga panjang totalnya menjadi 512 bit.
    padding = bits
    while len(padding) % 512 != 448:
        padding += "0"
    padding += '{0:064b}'.format(len(bits) - 1)

    # chunks bertujuan mengambil sebagian bit dari bit yang telah di-paddding
    def chunks(l, n):
        return [l[i:i + n] for i in range(0, len(l), n)]

    # rol mengembalikan nilai array dengan indeks 32 lebih kecil dari syarat
    # yang memenuhi syarat
    def rol(n, b):
        return ((n << b) | (n >> (32 - b))) & 0xffffffff

    # loop berikut ini menghash bit-bit pada padding menggunakan header
    for c in chunks(padding, 512):
        words = chunks(c, 32)
        w = [0] * 80
        for n in range(0, 16):
            w[n] = int(words[n], 2)
        for i in range(16, 80):
            w[i] = rol((w[i - 3] ^ w[i - 8] ^ w[i - 14] ^ w[i - 16]), 1)

        a = h0
        b = h1
        c = h2

        # Main loop yang diadaptasi dari loop hashing MD5 (loop MD5
        # menggunakan range 0 sampai 63)
        for i in range(0, 80):
            if 0 <= i <= 19:
                f = (b & c)
                k = 0x5A827999
            elif 20 <= i <= 39:
                f = b ^ c
                k = 0x6ED9EBA1
            elif 40 <= i <= 59:
                f = (b & c)
                k = 0x8F1BBCDC
            elif 60 <= i <= 79:
                f = b ^ c
                k = 0xCA62C1D6

            temp = rol(a, 5) + f + k + w[i] & 0xffffffff
            c = rol(b, 30)
            b = a
            a = temp

        # revisi nilai h0, h1, dan h2 berdasarkan hasil setiap perulangan
        h0 = h0 + a & 0xffffffff
        h1 = h1 + b & 0xffffffff
        h2 = h2 + c & 0xffffffff

    # mengeluarkan output hashing dengan menggabungkan 8 karakter pertama dari h0, h1, dan h2
    return '%08x%08x%08x' % (h0, h1, h2)
