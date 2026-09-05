def ficha(nome = '<Desconhecido>', gols = 0):
    if nome == '':
        nome = '<Desconhecido>'
    if gols == '':
        gols = 0
    print(f'O jogador {nome} fez {gols} gol(s) no campeonato.')


nome = str(input('Nome do Jogador: '))
gols = input('Número de Gols: ')
ficha(nome, gols)
