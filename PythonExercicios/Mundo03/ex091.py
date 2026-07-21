from random import randint
from time import sleep
print(f'{"Jogando dados":-^30}\n')
jogo = {'Jogador 1': randint(1,6), 'Jogador 2': randint(1,6), 
        'Jogador 3': randint(1,6), 'Jogador 4': randint(1,6)}
for jogador, rolagem in jogo.items():
    print(f'O {jogador} tirou {rolagem}')
    sleep(1)
print('\nRanking dos jogadores:')
