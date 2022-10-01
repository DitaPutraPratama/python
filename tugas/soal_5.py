nama = input('Masukan Nama :')
daftarNilai = []

for i in range(7):
    nilai = int(input(f'masukan nilai {i+1} :'))
    daftarNilai.append(nilai)

rata=sum(daftarNilai)/len(daftarNilai)
nilaiTerendah = min(daftarNilai)
nilaitinggi = max(daftarNilai)

print(f'Nama Mahasiswa :{nama}')
print(f'Daftar Nilai :{daftarNilai}')
print(f'Nilai terendah :{nilaiTerendah}')
print(f'Nilai tertinggi :{nilaitinggi}')
print(f'Nilai Rata Rata :{round(rata, 1)}')
