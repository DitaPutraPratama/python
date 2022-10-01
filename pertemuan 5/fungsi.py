'''def adalah fungsi'''
# print('selamat pagi ,hari ini kita makan')
# print('selamat siang ,hari ini kita makan')
# print('selamat sore ,hari ini kita makan')
# print('selamat malam ,hari ini kita makan')

''''''

# def selamat(waktu):
#     print(f'selamat {waktu}, hari ini kita pergi')

# selamat('pagi')
# selamat('siang')
# selamat('sore')
# selamat('malam')

''''''

# def salam(nama):
#     print(f'selamat datang {nama}')

# inputan=input('masukan nama :')
# salam(inputan)
''''''


# def luasBangunan(panjang, lebar, nama):
#     luas = float(panjang)*float(lebar)
#     print(
#         f'luas dari bangunan {nama} dengan panjang {panjang}m dan lebar {lebar}m adalah {round(luas, 2)}m')


# nm = input('masukan nama bangunan :')
# pjg = input('masukan panjang :')
# lbr = input('masukan lebar :')
# luasBangunan(panjang=pjg, lebar=lbr, nama=nm)
''''''
# def luasSegi(panjang, lebar):
#     luas = float(panjang)*float(lebar)
#     return luas

# pjg = input('masukan panjang :')
# lbr = input('masukan lebar :')

# hasil=luasSegi(panjang=pjg, lebar=lbr)
# print(f'luas dari panjang {pjg} dan lebar {lbr} adalah luas {hasil}')
''''''
# def hitngPersegiPanjang():
#     pjg = input('masukan panjang :')
#     lbr = input('masukan lebar :')

#     def hitungLuas(panjang, lebar):
#         return float(panjang)*float(lebar)

#     def hitungKeliling(panjang, lebar):
#         return 2*float(panjang)+float(lebar)

#     luas = hitungLuas(pjg, lbr)
#     keliling = hitungKeliling(pjg, lbr)
#     print(f'luas dari panjang {pjg} dan lebar {lbr} adalah {luas}')
#     print(f'keliling dari panjang {pjg} dan lebar {lbr} adalah {keliling}')


# hitngPersegiPanjang()
''''''


def kalkulator():
    angka1 = int(input('masukan angka pertama : '))
    op = input(
        f'masukan operator\n[pertambah : +]\n[pengurangan : -]\n[pembagian : /]\n[perkalian : *] \n operator :')
    angka2 = int(input('masukan angka kedua :'))

    if op == '+':
        hasil = angka1 + angka2
        print(f'hasil perhitungan : {hasil}')
    elif op == '-':
        hasil = angka1-angka2
        print(f'hasil perhitungan : {hasil}')
    elif op == '*':
        hasil = angka1 * angka2
        print(f'hasil perhitungan : {hasil}')
    elif op == '/':
        hasil = angka1 / angka2
        print(f'hasil perhitungan : {hasil}')


kalkulator()
