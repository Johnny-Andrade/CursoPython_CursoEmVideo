linha1 = []
linha2 = []
linha3 = []
matriz = [linha1, linha2, linha3]
c = pares = soma3 = 0
for indice in range(0,3):
    l1 = int(input(f'Digite um valor para [0, {indice}]: '))
    linha1.append(l1)
    if indice == 2:
        soma3 += l1
for indice in range(0,3):
    l2 = int(input(f'Digite um valor para [1, {indice}]: '))
    if indice == 0:
        maior = l2
    elif l2 > maior:
        maior = l2
    linha2.append(l2)
    if indice == 2:
        soma3 += l2
for indice in range(0,3):
    l3 = int(input(f'Digite um valor para [2, {indice}]: '))
    linha3.append(l3)
    if indice == 2:
        soma3 += l3
print('-='*20)
for indice, item in enumerate(matriz):
    for valor in matriz[indice]:
        print(f'[ {valor} ]', end=' ')
        c += 1
        if c % 3 == 0:
            print()
        if valor % 2 == 0:
            pares += valor
print('-='*20)
print(f'A soma dos valores pares é {pares}')
print(f'A soma dos valores da terceira coluna é {soma3}')
print(f'O maior valor da segunda linha é {maior}')
