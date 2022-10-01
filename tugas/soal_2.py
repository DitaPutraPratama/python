tgb = int(input('masukan tinggi badan anda (cm) :'))
bb = int(input('masukan berat badan anda (kg) :'))
bmi = bb/((tgb/100)**2)
print(f'Nilai BMI anda adalah : {round(bmi, 1)}')

if bmi <= 18.5:
    print('Berdasarkan nilai BMI, anda Terlalu kurus')
elif bmi >= 18.6 and bmi <= 25:
    print('Berdasarkan nilai BMI, anda Ideal')
elif bmi >= 25.1:
    print('Berdasarkan nilai BMI, anda Terlalu gemuk')
