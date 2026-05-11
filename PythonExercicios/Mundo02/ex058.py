from random import randint
from time import sleep
palpites = 1
print('-='*20)
print('Adivinhe o número!')
print('-='*20)
sleep(.3)
print('O computador vai pensar em um número de 0 a 10...')
sleep(1)
ganhou = False
escolhido = randint(0,10)
while ganhou != True:
    n = int(input('Tente adivinhar: '))
    if n == escolhido:
        ganhou = True
    else:
        palpites += 1
        print('Errou! Tente novamente.')
if palpites == 1:
    print('De primeira!! O número era {}, mesmo.'.format(escolhido))
else:
    print('Acertou! O número era {}. Você precisou de {} palpites.'.format(escolhido, palpites))
