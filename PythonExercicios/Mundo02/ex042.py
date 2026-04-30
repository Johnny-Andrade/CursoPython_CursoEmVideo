print('-='*20)
print('Validação de retas de um triângulo V2! ')
print('-='*20)
r1 = float(input('Digite o valor da 1° reta do triângulo: '))
r2 = float(input('Digite o valor da 2° reta do triângulo: '))
r3 = float(input('Digite o valor da 3° reta do triângulo: '))
if (r1 < r2 + r3) and (r2 < r1 + r3) and (r3 < r1 + r2):
    print('\033[32mTemos um triângulo válido.\033[m')
    if r1 == r2 == r3:
        print('Além disso, ele é \033[33mEquilátero.\033[m')
    elif (r1 == r2 != r3) or (r2 == r3 != r1) or (r1 == r3 != r2):
        print('Além disso, ele é \033[34mIsósceles.\033[m')
    else: 
        print('Além disso, ele é \033[35mEscaleno.\033[m')
else:
    print('\033[31mNão é um triângulo válido...\033[m')
