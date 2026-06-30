linha1 = []
linha2 = []
linha3 = []
matriz = [linha1, linha2, linha3]
for indice in range(0,3):
    linha1.append(int(input(f'Digite um valor para [0, {indice}]: ')))
for indice in range(0,3):
    linha2.append(int(input(f'Digite um valor para [1, {indice}]: ')))
for indice in range(0,3):
    linha3.append(int(input(f'Digite um valor para [2, {indice}]: ')))
print('-='*20)
print(f'''[ {matriz[0][0]} ] [ {matriz[0][1]} ] [ {matriz[0][2]} ]
[ {matriz[1][0]} ] [ {matriz[1][1]} ] [ {matriz[1][2]} ]
[ {matriz[2][0]} ] [ {matriz[2][1]} ] [ {matriz[2][2]} ]
''')
