print('Validação de retas de um triângulo! ')
r1 = int(input('Digite o valor da 1° reta do triângulo: '))
r2 = int(input('Digite o valor da 2° reta do triângulo: '))
r3 = int(input('Digite o valor da 3° reta do triângulo: '))
valid = False

if r1 < r2+r3:
    valid = 1
    if r2 < r1+r3:
        if r3 < r1+r2:
            valid = True
        else:
            valid = False
    else:
        valid = False

if valid:
    print('É possível fazer um triângulo!')
else:
    print('Triângulo inválido! Utilize outros valores.')
