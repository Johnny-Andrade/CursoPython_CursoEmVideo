ficha = list()
while True:
    nome = str(input('Nome: ')).strip()
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    ficha.append([nome, [nota1, nota2], media])
    conf = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    while conf not in 'SN':
        conf = str(input('\033[31m[ERRO]\033[m Quer continuar? [S/N]: ')).strip().upper()[0]
    if conf == 'N':
        break
print('-='*30)
print(f'{'N°':<4}{'Nome':<10}{'Média':>8}')
print('--'*13)
for indice, aluno in enumerate(ficha):
    print(f'{indice+1:<4}{aluno[0]:<10}{aluno[2]:>8.1f}')
while True:
    print('-'*35)
    opc = int(input('Quer ver as notas de qual aluno? [999 Finaliza]: '))
    if opc == 999:
        break
    if opc <= len(ficha):
        print(f'Notas de {ficha[opc-1][0]} são {ficha[opc-1][1]}')
print('\nFINALIZANDO...\n')
print('<<< VOLTE SEMPRE >>>')
