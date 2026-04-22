print('-='*20)
print('Validação de retas de um triângulo! ')
print('-='*20)
r1 = float(input('Digite o valor da 1° reta do triângulo: '))
r2 = float(input('Digite o valor da 2° reta do triângulo: '))
r3 = float(input('Digite o valor da 3° reta do triângulo: '))
valid = False

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    valid = True
else:
    valid = False

if valid:
    print('É possível fazer um triângulo!')
else:
    print('Triângulo inválido! Utilize outros valores.')
