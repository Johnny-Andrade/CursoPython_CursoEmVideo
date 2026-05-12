from random import randint
from time import sleep
print('-='*20)
print('Adivinhe o número!')
print('-='*20)
sleep(.3)
print('O computador vai pensar em um número de 0 a 10...')
sleep(1)
escolhido = randint(0,10)
palpites = 0
ganhou = False
while not ganhou:
    n = int(input('Tente adivinhar: '))
    palpites += 1
    if n == escolhido:
        ganhou = True
    elif n > escolhido:
        print('Menos! Tente novamente.')
    elif n < escolhido:
        print('Mais! Tente novamente')
if palpites == 1:
    print('De primeira!! O número era {}, mesmo.'.format(escolhido))
else:
    print('Acertou! Era {}. Você precisou de {} palpites.'.format(escolhido, palpites))
