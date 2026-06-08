tupla = (int(input('Digite um número: ')), int(input('Digite um número: ')), int(input('Digite um número: ')), int(input('Digite um número: ')))
pares = 0
if tupla.count(9) > 0:
    print('O número 9 apareceu {} vezes'.format(tupla.count(9)))
else:
    print('Não há número 9.')
if tupla.count(3) > 0:
    print('O número 3 apareceu primeiro na {}° posição.'.format(tupla.index(3)+1))
else:
    print('Não há número 3.')
for num in tupla:
    if num % 2 == 0:
        pares += 1
        numpares1 = (num, )
        if pares == 1:
            todospares = numpares1
        else:
            todospares = todospares + numpares1
if pares > 0:
    print(f'Existem {pares} números pares, sendo eles {todospares}')
else:
    print('Não há números pares.')
