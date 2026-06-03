from random import randint
tupla = (randint(0,10),randint(0,10),randint(0,10),randint(0,10),randint(0,10))
print('Os valores sorteados foram: {}'.format(tupla))
print('O menor valor foi: {}'.format(sorted(tupla)[-1]))
print('O maior valor foi: {}'.format(sorted(tupla)[0]))
