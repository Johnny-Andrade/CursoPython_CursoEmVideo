tupla = (int(input('Digite um número: ')), int(input('Digite um número: ')), int(input('Digite um número: ')), int(input('Digite um número: ')))
pares = 0
if tupla.count(9) > 0:
    print('O número 9 apareceu {} vezes'.format(tupla.count(9)))
else:
    print('Não há nenhum número 9.')
print('O número 3 apareceu primeiro na {}° posição.'.format(tupla.index(3)+1))
for num in tupla:
    if num % 2 == 0:
        pares += 1
if pares > 0:
    print('Existem {} números pares'.format(pares))
else:
    print('Não há números pares.')
