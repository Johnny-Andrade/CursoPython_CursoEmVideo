from time import sleep
def maior(*valores):
    print('-='*20)
    print(f'Analisando os valores passados...')
    if len(valores) == 0:
        maior = 0
    for indice, item in enumerate(valores):
        if indice == 0:
            maior = item
        else:
            if maior < item:
                maior = item
        print(item, end=' ', flush = True)
        sleep(.3)
    print(f'\nForam informados {len(valores)} valores ao todo.')
    print(f'O maior valor informado foi {maior}.')
    sleep(.5)


maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()
