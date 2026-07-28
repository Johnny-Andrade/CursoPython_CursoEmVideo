totgol = ngol = 0
jogadores = []
while True:
    nome = str(input('Diga o nome do jogador: ')).strip()
    npart = int(input('Quantas partidas ele jogou? '))
    gols = list()
    for p in range(0, npart):
        ngol = int(input(f'Quantos gols {nome} fez no {p+1}° jogo? '))
        gols.append(ngol)
        totgol += ngol
    conf = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    while conf not in 'SN':
        conf = str(input('\033[31m[ERRO]\033[m Quer continuar? [S/N]: ')).strip().upper()[0]
    print('--'*20)
    dados = {'Nome': nome, 'NGols': gols, 'Total': totgol}
    jogadores.append(dados.copy())
    if conf == 'N':
        break
print('-='*30)
print(f'cod {"nome":<15} {"gols":<15} total')
print('--'*25)
for indice, item in enumerate(jogadores):
    print(f'{indice:>3}',end=' ')
    print(f'{jogadores[indice]["Nome"]:<15}',end=' ')
    print(f'{str(jogadores[indice]["NGols"]):<15}',end=' ')
    print(f'{jogadores[indice]["Total"]}')
print('--'*25)
while True:
    escolha = int(input('Mostrar dados de qual jogador? [999 = FIM]: '))
    while ((escolha > len(jogadores)) or (escolha < 0)) and escolha != 999:
        escolha = int(input('\033[31m[ERRO]\033[m Mostrar dados de qual jogador? [999 = FIM]: '))
    if escolha == 999:
            break
    print(f'LEVANTAMENTO DO JOGADOR {jogadores[escolha]["Nome"]}')
    for indice, item in enumerate(jogadores[escolha]["NGols"]):
        print(f'No jogo {indice+1} fez {item} gols.')
    print('--'*20)
print(f'{"<<< VOLTE SEMPRE >>>"}')
