from random import randint
from time import sleep
print('--'*20)
print('Par ou Ímpar!')
print('--'*20)
cont = soma = 0
while True:
    print('\nO computador vai escolher um número...')
    sleep(.3)
    computador = randint(1,10)
    numJogador = int(input('Escolha um número: '))
    escolha = str(input('Escolha Par ou Ímpar [P/I]: ')).strip().upper()[0]
    while escolha != 'P' and escolha != 'I':
        escolha = str(input('[ERRO] Escolha Par ou Ímpar [P/I]: ')).strip().upper()[0]
    print('--'*20)
    soma = computador + numJogador
    print(f'Você escolheu {numJogador} e o computador {computador}. Tivemos total de {soma}.', end='')
    if soma % 2 == 0:
        print(' Logo, deu Par.')
    else:
        print(' Logo, deu Ímpar.')
    print('--'*20)
    if escolha == 'P' and soma % 2 != 0:
        print('Você PERDEU!')
        break
    elif escolha == 'I' and soma % 2 == 0:
        print('Você PERDEU!')
        break
    cont += 1
print(f'Fim de jogo! Você venceu {cont} vezes.')
