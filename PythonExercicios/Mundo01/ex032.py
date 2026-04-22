ano = int(input('Digite um ano: '))
if ano % 4 == 0:
    print('{} é um ano BISSEXTO!'.format(ano))
else:
    print('{} NÃO é um ano bissexto...'.format(ano))
