def aumentar(n, perc = 10, form = False):
    perc = (perc/100)+1
    if form == True:
        return f'R${n*perc:.2f}'
    return n*perc
    

def diminuir(n, perc = 10, form = False):
    perc = 1-(perc/100)
    if form == True:
        return f'R${n*perc:.2f}'
    return n*perc
    

def dobro(n, form = False):
    if form == True:
        return f'R${n*2:.2f}'
    return n*2


def metade(n, form = False):
    if form == True:
        return f'R${n/2:.2f}'
    return n/2


def moeda(n):
    return f'R${n:.2f}'


def resumo(n, aum=10, redu=10):
    print('--'*15)
    print(f'{"RESUMO DO VALOR":^30}')
    print('--'*15)
    print(f'Preço analisado: {moeda(n):>10}')
    print(f'Dobro do preço: {dobro(n, True):>10}')
    print(f'Metade do preço: {metade(n, True):>10}')
    print(f'{aum}% de aumento: {aumentar(n, aum, True):>10}')
    print(f'{redu}% de redução: {diminuir(n, redu, True):>10}')
    print('--'*15)

