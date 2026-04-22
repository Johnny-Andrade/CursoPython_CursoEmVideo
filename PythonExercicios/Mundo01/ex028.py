from random import randint
from time import sleep
escolhido = randint(0,5) #Número é escolhido
print('-=-'*20)
print('O computador escolheu um número, vamos ver se você escolhe o mesmo?')
print('-=-'*20)
num = int(input('\nDigite um número de 0 a 5: '))
print('Processando...')
sleep(2)
if num == escolhido:
    print('Vocês escolheram igual. Que legal!')
else:
    print('Que pena, o computador escolheu {}...'.format(escolhido))
