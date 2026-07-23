totPes = idadeMed = 0
mulheres = list()
while True:
    totPes += 1 
    nome = str(input('Digite o nome: ')).strip()
    sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]
    while sexo not in 'FM':
        sexo = str(input('\033[31m[ERRO]\033[m Sexo: [M/F] ')).strip().upper()[0]
    if sexo == 'F':
        mulheres.append(nome)
    idade = int(input('Digite a idade: '))
    idadeMed += idade
    conf = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    while conf not in 'SN':
        conf = str(input('\033[31m[ERRO]\033[m Deseja continuar? [S/N] ')).strip().upper()[0]
    if conf == 'N':
        idadeMed /= totPes
        break
print('-='*20)
print(f'- O grupo tem {totPes} pessoas.')
print(f'- A média de idade é de {idadeMed} anos.')
print(f'As mulheres cadastradas foram: ', end='')
for item in mulheres:
    print(f'{item} ', end='')
print()
