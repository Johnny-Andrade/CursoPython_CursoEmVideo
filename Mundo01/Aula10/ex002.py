nota1 = float(input('Digite a nota da primeira prova: '))
nota2 = float(input('Digite a nota da segunda prova: '))
media = (nota1+nota2)/2

print('A sua média foi {:.1f}'.format(media))
if media <6:
    print('Você não passou...')
else:
    print('Você passou!')
