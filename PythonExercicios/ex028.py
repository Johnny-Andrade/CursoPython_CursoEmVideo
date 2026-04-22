from random import randint
escolhido = randint(0,5)
num = int(input('Digite um número de 0 a 5: '))
print('Agora, o computador escolheu um número, vamos ver se você escolheu o mesmo...')
if num == escolhido:
    print('Vocês escolheram igual. Que legal!')
else:
    print('Trompete? Som triste, foram diferentes...')
