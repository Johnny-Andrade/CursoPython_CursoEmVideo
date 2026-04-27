nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
media = (nota1 + nota2)/2
if media <5:
    print('Sua média é {}, você foi \033[31mREPROVADO\033[m'.format(media))
elif media >=5 and media <7:
    print('Sua média é {}, você está de \033[33mRECUPERAÇÃO\033[m'.format(media))
else:
    print('Sua média é {}, você foi \033[32mAPROVADO\033[m'.format(media))
