'''1'''
nilaiMhs=[2,10,9,99,90,80,78,54,77,66,55,23,44,43,32,12]
nilaiterendah=(min(nilaiMhs))
nilaitertinggi=(max(nilaiMhs))
nilaiRt= (sum(nilaiMhs))/(len(nilaiMhs))

print(f'nilai terendah : {nilaiterendah}')
print(f'nilai tertinggi : {nilaitertinggi}')
print(f'nilai rata rata : {nilaiRt}')
print( )
'''2'''
buah1=['pisang','apel','duku','pepaya','melon']
buah2=['semangka','tomat','timun','leci','suwek']
listbaru=buah1+buah2
print(listbaru)
listbaru.insert(5,'buah naga')
print(listbaru)