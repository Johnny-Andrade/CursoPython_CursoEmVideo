print('-='*20)
print('Analisador de pesos!')
print('-='*20)
maior = 0
menor = 0
for pessoa in range(1,6):
    peso = float(input('Qual o peso da {}° pessoa? '.format(pessoa)))
    if pessoa == 1:
        maior = peso
        menor = peso
    else:    
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('O maior peso lido foi \033[34m{:.1f}\033[mkg\nO menor peso lido foi \033[36m{:.1f}\033[mkg.'.format(maior, menor))
