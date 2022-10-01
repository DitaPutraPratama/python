'''While loop'''
# num=7
# c=1

# while c <= num: #kondisi perulangan
#     print('mencetak ke', c)

#     c=c+1#menambah counter

# # print selesai
# print('cetak selesai')
# print()

# num = 21
# c = 1
# print('tabel perkalian dari', num)
# while c <= 10:
#     hasil = num*c
#     print(num, 'x', c, '=', hasil)
#     c += 1
# print()

list = [3, 5, 1, 4, 6]
listBaru = []
while list:
    print(list)
    listBaru.append((list.pop()))
print(listBaru)
print()

'''for loop'''
# for i in range(10):
#     print('cetak ke', i)
# print()

# for index in range(4,10):
#     print('cetak ke', index)
# print()

# for index in range(4,20, 2):
#     print('cetak ke', index)
# print()

listBuah = ['apel', 'mangga', 'kates']
for buah in listBuah:
    print(f'cetak {buah}')
# print()

# listBuah=['apel','mangga','kates']
# for buah in listBuah:
#     if buah == 'kates':
#         print(f'beli {buah} 10')
#     else:
#         print(f'beli {buah} 5')
# print()

# listKopi=['late','kapucino','amerikano','tubruk']
# listType=['ice','hot']

# for type in listType:
#     for kopi in listKopi:
#         print(f'{type} {kopi}')
# print()

# jmlJamMain=0
# while jmlJamMain<5:
#     jmlJamMain+=1
#     print(f'andi main hero {jmlJamMain} jam')
# else:
#     print(f'andi hannya boleh main hero {jmlJamMain} jam')
# print()

# listNama =['budi','andi']
# listHero=['tigreal','gatot','mia']

# for nama in listNama:
#     for hero in listHero:
#         print(f'{nama} suka main {hero}')
#     else:
#         print(f'ternyata {listNama[0]} dan {listNama[0]} adalah pemain tank')
