from random import randint
from time import sleep
from operator import itemgetter
print(f'{"Jogando dados":-^30}\n')
jogo = {'Jogador 1': randint(1,6), 'Jogador 2': randint(1,6), 
        'Jogador 3': randint(1,6), 'Jogador 4': randint(1,6)}
for jogador, rolagem in jogo.items():
    print(f'O {jogador} tirou {rolagem} no d6.')
    sleep(.8)
print()
ranking = list()
ranking = sorted(jogo.items(), key = itemgetter(1), reverse= True)
print('-='*20)
print(' == RANKING DOS JOGADORES ==\n')
for indice, valor in enumerate(ranking): # Pois o processo cria uma lista e não dicionario
    print(f'  {indice+1}° Lugar: {valor[0]} com {valor[1]}.')
    sleep(.8)
