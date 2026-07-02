from random import randint
from time import sleep
sorteio = []
todossort = []
print('--'*20)
print('Auxílio Mega Sena')
print('--'*20)
numjogos = int(input('\nDigite quantos jogos serão: '))
for cont in range(0, numjogos):
    while len(sorteio) < 6:
        aleatorio = randint(1, 60)
        if aleatorio not in sorteio:
            sorteio.append(aleatorio)
    sorteio.sort()
    todossort.append(sorteio[:])
    sorteio.clear()
print(f'\nSorteando {numjogos} jogos!\n')
for indice, item in enumerate(todossort):
    print(f'Jogo {indice+1}: {item}')
    sleep(.5)
print(f'\nBOA SORTE!\n')
