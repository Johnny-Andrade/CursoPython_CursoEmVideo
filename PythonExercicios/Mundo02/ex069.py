homens = mulheres = adultos = 0
while True:
    print('--'*20)
    print('CADASTRE PESSOAS')
    print('--'*20,'\n')
    idade = int(input('Digite a Idade da pessoa: '))
    sexo = str(input('Digite o Sexo da pessoa [M/F]: ')).strip().upper()[0]
    while sexo != 'M' and sexo != 'F':
        sexo = str(input('\033[31m[ERRO]\033[mDigite o Sexo da pessoa [M/F]: ')).strip().upper()[0]
    if sexo == 'M':
        homens += 1
    if idade >= 18:
        adultos += 1
    if sexo == 'F' and idade < 20:
        mulheres += 1
    continuar = str(input('\nDeseja continuar? [S/N]: ')).strip().upper()[0]
    while continuar != 'S' and continuar != 'N':
        continuar = str(input('\033[31m[ERRO]\033[mDeseja continuar? [S/N]: ')).strip().upper()[0]
    if continuar == 'N':
        break
print('\nAo todo, tivemos:')
print(f'{adultos} pessoas com 18 anos ou mais.\n{homens} Homens cadastrados.\n{mulheres} Mulheres com menos de 20 anos.')
