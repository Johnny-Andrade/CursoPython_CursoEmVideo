valores = [] # valores = list() também funciona
for cont in range(0, 5):
    valores.append(int(input('Digite um Valor: ')))
for v in valores:
    print(f'{v} > ',end='')
print('Fim!\n')
for p, v in enumerate(valores):
    print(f'Na posição {p} encontrei o valor {v}...')
