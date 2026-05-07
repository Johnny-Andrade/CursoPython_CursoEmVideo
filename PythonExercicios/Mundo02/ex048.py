print('Entre 1 e 500, faremos a soma dos múltiplos de 3 ímpares: ')
soma = 0
quant = 0
for c in range(3, 501, 3):
    if c%2 != 0:
        soma += c
        quant += 1
print('A soma dos \033[33m{}\033[m valores que correspondem é igual a \033[32m{}\033[m.'.format(quant, soma))
