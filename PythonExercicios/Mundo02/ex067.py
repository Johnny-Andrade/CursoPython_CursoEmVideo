print('--'*20)
print('Tabuada v3')
print('Digite um número negativo para finalizar')
while True:
    print('--'*20)
    n = int(input('Digite um número para a tabuada: '))
    print('--'*20)
    if n < 0:
        break
    for c in range(1,11):
        print(f'{c:2} x {n} = {c*n}')
print('Obrigado por nos escolher!')
print('--'*20)
