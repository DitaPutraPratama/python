nama = input('masukan nama anda :')
lahir = int(input('masukan tahun kelahiran anda :'))

if lahir < 1944:
    print('belum terkategori')
elif lahir >= 1944 and lahir <= 1964:
    print(f'{nama} berdasarkan tahun lahir, anda termasuk generasi Baby boomer')
elif lahir >= 1965 and lahir <= 1979:
    print(f'{nama} berdasarkan tahun lahir, anda termasuk generasi X (Bust)')
elif lahir >= 1980 and lahir <= 1994:
    print(f'{nama} berdasarkan tahun lahir, anda termasuk generasi Y (Milenial)')
elif lahir >= 1995 and lahir <= 2015:
    print(f'{nama} berdasarkan tahun lahir, anda termasuk generasi Z (Internet)')
elif lahir > 2015:
    print('belum terkategori')
