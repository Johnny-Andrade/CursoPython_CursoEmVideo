print('--'*20)
print('Tabuada v3')
print('Digite um número negativo para finalizar')
while True:
    cont = 1
    print('--'*20)
    n = int(input('Digite um número para a tabuada: '))
    print('--'*20)
    if n < 0:
        break
    while cont <= 10:
        print(f'{cont:2} x {n} = {cont*n}')
        cont += 1
print('Obrigado por nos escolher!')
print('--'*20)
