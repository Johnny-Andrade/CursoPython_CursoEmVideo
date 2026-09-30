def aumentar(n, perc = 10, form = False):
    perc = (perc/100)+1
    res = n*perc
    return res if not form else moeda(n*perc)
    

def diminuir(n, perc = 10, form = False):
    perc = 1-(perc/100)
    res = n*perc
    return res if not form else moeda(res)
    

def dobro(n, form = False):
    res = n*2
    return res if not form else moeda(res)


def metade(n, form = False):
    res =  n/2
    return res if not form else moeda(res)


def moeda(n, moeda='R$'):
    return f'{moeda}{n:.2f}'.replace('.',',')


def resumo(n, aum=10, redu=10):
    print('-'*36)
    print('RESUMO DO VALOR'.center(36))
    print('-'*36)
    print(f'Preço analisado: \t{moeda(n)}')
    print(f'Dobro do preço: \t{dobro(n, True)}')
    print(f'Metade do preço: \t{metade(n, True)}')
    print(f'{aum}% de aumento: \t{aumentar(n, aum, True)}')
    print(f'{redu}% de redução: \t{diminuir(n, redu, True)}')
    print('-'*36)

