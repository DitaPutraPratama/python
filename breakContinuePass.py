for i in range(10):
    if i == 3:
        print('stop disini', i)
        break
    print('cetak ke', i)
print()

listJam = [8, 9, 10, 11, 12, 13, 14, 15]

for jam in listJam:
    if jam == 12 or jam == 13:
        continue
    print('andi main game ', jam)
