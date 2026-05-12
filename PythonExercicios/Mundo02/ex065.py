continuar = 'S'
contador = 0
soma = 0
while continuar == 'S':
    num = int(input('Insira um número: '))
    continuar = str(input('Você deseja continuar? [S/N]: ')).strip().upper()
    if continuar != 'N' and continuar != 'S':
        while continuar != 'N' and continuar != 'S':
            continuar = str(input('[Erro] Deseja continuar? [S/N]: ')).strip().upper()
    contador += 1
    soma += num
    if contador == 1:
        maior = menor = num
    if maior < num:
        maior = num
    if menor > num:
        menor = num
print('Foram digitados {} números, dentre eles, o maior é {} e o menor é {}.'.format(contador, maior, menor))
print('Fazendo a média de todos os valores digitados, temos {:.2f}.'.format(soma/contador))
