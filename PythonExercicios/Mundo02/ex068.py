from random import randint
from time import sleep
print('--'*20)
print('Par ou Ímpar!')
print('--'*20)
contVit = soma = 0
while True:
    print('\nO computador vai escolher um número...')
    sleep(.3)
    computador = randint(0,10)
    numJogador = int(input('Escolha um número: '))
    escolha = str(input('Escolha Par ou Ímpar [P/I]: ')).strip().upper()[0]
    while escolha not in 'PpIi':
        escolha = str(input('\033[31m[ERRO]\033[m Escolha Par ou Ímpar [P/I]: ')).strip().upper()[0]
    print('--'*20)
    soma = computador + numJogador
    print(f'Você escolheu {numJogador} e o computador {computador}. Tivemos total de {soma}. ', end='')
    print('Logo, deu Par!' if soma % 2 == 0 else 'Logo, deu Ímpar')
    print('--'*20)
    if (escolha == 'P' and soma % 2 != 0) or (escolha == 'I' and soma % 2 == 0):
        print('Você PERDEU!')
        break
    contVit += 1
print(f'Fim de jogo. ',end='')
if contVit == 0:
    print('Eita ferro... Não venceu nenhuma.')
elif contVit == 1:
    print('Você venceu apenas uma vez...')
else:
    print(f'Você venceu {contVit} vezes!')
