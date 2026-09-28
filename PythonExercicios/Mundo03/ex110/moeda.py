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
    print('--'*15)
    print(f'{"RESUMO DO VALOR":^30}')
    print('--'*15)
    print(f'Preço analisado: {moeda(n):>10}')
    print(f'Dobro do preço: {dobro(n, True):>10}')
    print(f'Metade do preço: {metade(n, True):>10}')
    print(f'{aum}% de aumento: {aumentar(n, aum, True):>10}')
    print(f'{redu}% de redução: {diminuir(n, redu, True):>10}')
    print('--'*15)

