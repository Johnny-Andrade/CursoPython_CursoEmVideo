from random import randint
tupla = (randint(0,10),randint(0,10),randint(0,10),randint(0,10),randint(0,10))
print('Os valores sorteados foram: ',end='')
for item in tupla:
    print(f'{item} ',end='')
print(f'\nO menor valor foi: {max(tupla)}')
print(f'O maior valor foi: {min(tupla)}')
