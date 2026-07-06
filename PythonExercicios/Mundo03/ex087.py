matriz = [[0, 0, 0],[0, 0, 0],[0, 0, 0]]
spar = scol = 0
for l in range(0, 3):
    for c in range(0, 3):
        valor = int(input(f'Digite um valor para a posição [{l}, {c}]: '))
        matriz[l][c] = valor
        if valor % 2 == 0:
            spar += valor
        if c == 2:
            scol += valor
        if l == 1:
            if c == 0 or valor > maior:
                maior = valor
print('-='*20)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()
print('-='*20)
print(f'A soma dos valores pares é {spar}')
print(f'A soma dos valores da terceira coluna é {scol}')
print(f'O maior valor da segunda linha é {maior}')
