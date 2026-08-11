from random import randint
from time import sleep
def sorteia(lst):
    listaTemp = list()
    print('Sorteando 5 valores da lista: ',end='')
    for cont in range(0,5):
        sorteado = randint(0,10)
        listaTemp.append(sorteado)
        print(sorteado, end=' ', flush = True)
        sleep(.5)
    print('PRONTO!')
    lst.clear()
    lst.extend(listaTemp)


def sorteiaPar(lista):
    soma = 0
    for item in lista:
        if item % 2 == 0:
            soma += item
    print(f'Sorteando os valores pares de {lista}, temos {soma}.')

    
numeros = list()
sorteia(numeros)
sorteiaPar(numeros)
