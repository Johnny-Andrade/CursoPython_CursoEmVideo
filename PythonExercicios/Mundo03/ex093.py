nome = str(input('Diga o nome do jogador: ')).strip()
npart = int(input('Quantas partidas ele jogou? '))
gols = list()
totgol = ngol = 0
for p in range(0, npart):
    ngol = int(input(f'Quantos gols {nome} fez no {p+1}° jogo? '))
    gols.append(ngol)
    totgol += ngol
print('--'*20)
dados = {'Nome': nome, 'NGols': gols, 'Total': totgol}
print(dados)
print('--'*20)
for key, value in dados.items():
    print(f'O campo {key} tem valor {value}')
print('-='*20)
print(f'O jogador {nome} jogou {npart} partidas.')
for indice, item in enumerate(gols):
    print(f'    => Na partida {indice+1}, fez {item} gols.')
print(f'Fez um total de {totgol} gols.')
