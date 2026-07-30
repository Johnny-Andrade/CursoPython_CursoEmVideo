dados = dict()
dados['Nome'] = str(input('Diga o nome do jogador: ')).strip()
npart = int(input('Quantas partidas ele jogou? '))
gols = list()
for p in range(0, npart):
    gols.append(int(input(f'Quantos gols {dados["Nome"]} fez no {p+1}° jogo? ')))
print('--'*20)
dados['NGols'] = gols
dados['Total'] = sum(gols)
print(dados)
print('--'*20)
for key, value in dados.items():
    print(f'O campo {key} tem valor {value}')
print('-='*20)
print(f'O jogador {dados['Nome']} jogou {npart} partidas.')
for indice, item in enumerate(dados['NGols']):
    print(f'    => Na partida {indice+1}, fez {item} gols.')
print(f'Fez um total de {dados['Total']} gols.')
