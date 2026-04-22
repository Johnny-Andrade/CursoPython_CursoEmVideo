from datetime import date
print('Análise de ano!')
ano = int(input('Digite um ano ou use 0 para o ano atual: '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('{} é um ano BISSEXTO!'.format(ano))
else:
    print('{} NÃO é um ano bissexto...'.format(ano))
