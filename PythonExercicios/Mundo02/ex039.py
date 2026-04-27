from datetime import date
ano = date.today().year
nasc = int(input('Digite o ano de seu nascimento: '))
idade = ano - nasc
if idade < 18:
    print('Ainda faltam {} para você precisar se alistar.'.format(18-idade))
elif idade >45:
    print('Você passou do limite, não pode mais se alistar.')
else:
    print('Você pode se alistar.')