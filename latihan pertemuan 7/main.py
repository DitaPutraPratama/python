from persegiFile import persegiPanjang
from persegiFile import persegi
pp = persegiPanjang()
ps = persegi()

print('Masukan pilihan\n1 untuk persegi panjang\n2 untuk persegi')
bangun = input('Masukan pilihan 1 atau 2 :')
if bangun == '1':
    print('Anda memilih persegi panjang')
    pp.nama = input('Masukan nama bangunan :')
    pp.panjang = int(input('Masukan panjang bangunan (m) :'))
    pp.lebar = int(input('Masukan lebar bangunan (m) :'))
    luas = pp.panjang*pp.lebar
    keliling = 2*(pp.panjang+pp.lebar)
    print(f'{pp.nama} memiliki panjang :{pp.panjang}m lebar :{pp.lebar}m luas :{luas}m dan keliling :{keliling}m')
elif bangun == '2':
    print('Anda memilih persegi')
    ps.nama = input('Masukan nama bangunan :')
    ps.panjangSisi = int(input('Masukan panjang bangunan (m) :'))
    luas = ps.panjangSisi*ps.panjangSisi
    keliling = 4*ps.panjangSisi
    print(f'{ps.nama} memiliki panjang :{ps.panjangSisi}m luas :{luas}m dan keliling :{keliling}m')
else:
    print('masukan sesuai dengan pilihan !')
