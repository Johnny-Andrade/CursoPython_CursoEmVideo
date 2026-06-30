linha1 = []
linha2 = []
linha3 = []
matriz = [linha1, linha2, linha3]
c = 0
for indice in range(0,3):
    linha1.append(int(input(f'Digite um valor para [0, {indice}]: ')))
for indice in range(0,3):
    linha2.append(int(input(f'Digite um valor para [1, {indice}]: ')))
for indice in range(0,3):
    linha3.append(int(input(f'Digite um valor para [2, {indice}]: ')))
print('-='*20)
[ {matriz[1][0]} ] [ {matriz[1][1]} ] [ {matriz[1][2]} ]
for indice, item in enumerate(matriz):
    for valor in matriz[indice]:
        print(f'[ {valor} ]', end=' ')
        c += 1
        if c % 3 == 0:
            print()
