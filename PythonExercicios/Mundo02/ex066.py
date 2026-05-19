soma = cont = 0
while True:
    n = int(input('[999 Finaliza]Digite um número inteiro: '))
    if n == 999:
        break
    soma += n
    cont += 1
print(f'Tivemos {cont} números e, somando-os, temos um total de {soma}.')
