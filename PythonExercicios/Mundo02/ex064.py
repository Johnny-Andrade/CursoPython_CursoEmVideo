soma = 0
num = 0
numq = 0
while num != 999:
    num = int(input('[999 Encerra] Digite um número inteiro: '))
    if num != 999:
        soma += num
        numq += 1
print('Fim! fora digitados {} números, e somando-os, temos {}.'.format(numq, soma))    
