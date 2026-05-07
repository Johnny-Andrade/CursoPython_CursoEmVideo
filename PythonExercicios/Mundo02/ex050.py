s = 0
quant = 0
for c in range (1,7):
    num = int(input('Digite um número inteiro: '))
    if num % 2 == 0:
        s += num
        quant += 1
print('A soma dos {} valores pares digitados é igual a {}.'.format(quant, s))
