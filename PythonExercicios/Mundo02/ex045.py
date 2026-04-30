from random import randint
from time import sleep
pcnum = randint(1,3)
print('-='*20)
print('Jokenpô!')
print('-='*20)
print('\nComputador escolhendo...')
sleep(1.5)
print('Feito!',end='')
jogador = str(input('Escolha PEDRA, PAPEL ou TESOURA: ')).strip().upper()
print('JO')
sleep(.5)
print('KEN')
sleep(1)
print('PO!!!')
sleep(.3)
if jogador == 'PEDRA':
    if pcnum == 1:
        print('Empate! Duas Pedras...')
    elif pcnum == 2:
        print('Perdeste! O computador tinha escolhido Papel!')
    else:
        print('Você ganhou! O computador escolheu Tesoura.')
elif jogador == 'PAPEL':
    if pcnum == 1:
        print('Você ganhou! O computador escolheu Pedra.')
    elif pcnum == 2:
        print('Empatamos! Dois Papéis...')
    else:
        print('Perdeu! Tesoura te cortou.')
elif jogador == 'TESOURA':
    if pcnum == 1:
        print('Perdeu! Tesoura quebrada pela Pedra computacional!')
    elif pcnum == 2:
        print('Ganhou!! Cortastes o Papel do computador!')
    else:
        print('Empatamos. Duas Tesouras...')
else:
    print('\033[31m[ERRO]\033[m Insira os comandos corretamente.')
