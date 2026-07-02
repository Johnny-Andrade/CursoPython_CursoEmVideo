todos = list()
nome = list()
notas = list()
Alunota = list()
while True:
    nomAl = str(input('Digite o nome do aluno: ')).strip()
    nome.append(nomAl)
    n1 = float(input('Digite a nota 1: '))
    n2 = float(input('Digite a nota 2: '))
    notas.append(n1)
    notas.append(n2)
    Alunota.append(nome[:])
    nome.clear()
    Alunota.append(notas[:])
    notas.clear()
    todos.append(Alunota[:])
    Alunota.clear()
    conf = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    while conf not in 'SN':
        conf = str(input('\033[31m[ERRO]\033[m Quer continuar? [S/N]: ')).strip().upper()[0]
    if conf == 'N':
        break
print('-='*15)
print(f'N° | {'NOME':<15} MÉDIA')
print('--'*15)
for indice, valor in enumerate(todos):
    media = ((todos[indice][1][0]+todos[indice][1][1])/2)
    print(f'{indice+1:<3}| {todos[indice][0][0]:<15} {media:>4.1f}')
print('--'*15)
while True:
    escolha = int(input('Mostrar notas de qual aluno? [999 Finaliza]: '))
    while ((escolha > len(todos)) and (escolha != 999)):
        escolha = int(input('\033[31m[ERRO]\033[m Mostrar notas de qual aluno? [999 Finaliza]: '))
    if escolha == 999:
        break
    else:
        print(f'Notas de {todos[escolha-1][0][0]} são {todos[escolha-1][1]}')
print('FINALIZANDO...\n')
print('<<< VOLTE SEMPRE >>>')
