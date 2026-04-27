print('-='*20)
print('Validação de retas de um triângulo! ')
print('-='*20)
r1 = float(input('Digite o valor da 1° reta do triângulo: '))
r2 = float(input('Digite o valor da 2° reta do triângulo: '))
r3 = float(input('Digite o valor da 3° reta do triângulo: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('\033[32mTemos\033[m um triângulo válido.')
    if r1 == r2 and r1 == r3:
        print('Além disso, ele é Equilátero.')
    elif (r1 == r2 and r2 != r3) or (r2 == r3 and r1 != r3) or (r1 == r3 and r3 != r2):
        print('Além disso, ele é Isósceles.')
    else: 
        print('Além disso, ele é Escaleno.')
else:
    print('\033[31mNão\033[m é um triângulo válido...')
