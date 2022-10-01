# def fungsiSaya():
#     x = 300
#     print(f'cetak {x}')

#     def fungsiDalam():
#         print(f'cetak {x} didalam fungsi')
#     fungsiDalam()

# fungsiSaya()
''''''
# user = input(f'masukan username :')
# pasw = int(input(f'masukan paswoed :'))

# def login(user, pasw):
#     if user == '@budi' and pasw == 12345:
#         print('BERHASIL MASUK')
#     else:
#         print('GAGAL MASUK')

# login(user, pasw)
''''''
# user = input(f'masukan username :')
# pasw = int(input(f'masukan paswoed :'))


# def login(user, pasw):
#     if user == 'budi' and pasw == 12345:
#         return 'berhasil masuk'
#     else:
#         return 'gagal masuk'


# cekLogin = login(user, pasw)
# print(cekLogin)
''''''

# x=102
# def fungsiSaya():
#     # global x
#     x = 300
#     print(f'cetak {x}')

#     def fungsiDalam():
#         print(f'cetak {x} didalam fungsi')
#     fungsiDalam()


# fungsiSaya()
# print(x)
''''''
def tambah (angka1, angka2):
    try:
        hasil=int(angka1)+int(angka2)
        return hasil
    except:
        print('anda harus masukan angka')

nomor1=input('masukan nomor ke 1 ')
nomor2=input('masukan nomor ke 2 ')

hasilTambah=tambah(angka1=nomor1, angka2=nomor2)
print(f'hasil={hasilTambah}')
