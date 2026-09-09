def ficha(nome = '<Desconhecido>', gol = 0):
    if nome == '':
        nome = '<Desconhecido>'
    if gol == '':
        gol = 0
    print(f'O jogador {nome} fez {gol} gol(s) no campeonato.')


nome = str(input('Nome do Jogador: ')).strip()
gols = str(input('Número de Gols: '))
if gols.isnumeric():
    gols = int(gols)
else:
    gols = 0
ficha(nome, gols)
