todos = []
pessoa = list()
while True:
    pessoa.append(str(input('Nome: ')).strip())
    peso = float(input('Peso: '))
    if len(todos) == 0:
        menPeso = maiPeso = peso
    elif peso > maiPeso:
        maiPeso = peso
    elif peso < menPeso:
        menPeso = peso
    pessoa.insert(0, peso)
    todos.append(pessoa[:])
    pessoa.clear()
    conf = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    while conf not in 'SN':
        conf = str(input('\033[31m[ERRO]\033[m Quer continuar? [S/N]: ')).strip().upper()[0]
    if conf == 'N':
        break
print('-='*20)
print(f'Ao todo, você cadastrou {len(todos)} pessoas')
print(f'O maior peso foi de {maiPeso}Kg. Que é o peso de ', end='')
for item in todos:
    if item[0] == maiPeso:
        print(f'[{item[1]}] ', end='')
print(f'\nO menor peso foi de {menPeso}Kg. Que é o peso de ', end='')
for item in todos:
    if item[0] == menPeso:
        print(f'[{item[1]}] ', end='')
