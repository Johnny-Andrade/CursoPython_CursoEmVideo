idadeMed = 0
pessoa = dict()
todos = list()
while True:
    pessoa.clear()
    pessoa["Nome"] = str(input('Digite o nome: ')).strip()
    pessoa["Sexo"] = str(input('Sexo: [M/F] ')).strip().upper()[0]
    while pessoa["Sexo"] not in 'FM':
        pessoa["Sexo"] = str(input('\033[31m[ERRO]\033[m Sexo: [M/F] ')).strip().upper()[0]
    pessoa['Idade'] = int(input('Digite a idade: '))
    idadeMed += pessoa['Idade']
    conf = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    while conf not in 'SN':
        conf = str(input('\033[31m[ERRO]\033[m Deseja continuar? [S/N] ')).strip().upper()[0]
    todos.append(pessoa.copy())
    if conf == 'N':
        idadeMed /= len(todos)
        break
print('-='*20)
print(f'A) O grupo tem {len(todos)} pessoas.')
print(f'B) A média de idade é de {idadeMed:5.2f} anos.')
print(f'C) As mulheres cadastradas foram: ', end='')
for item in todos:
    if item["Sexo"] == 'F':
        print(f'{item["Nome"]} ', end='')
print(f'\nD) Lista das pessoas com idade acima da média:')
for item in todos:
    if item["Idade"] > idadeMed:
        for key, value in item.items():
            print(f'{key} = {value}', end='; ')
        print()
print('<< ENCERRADO >>')
