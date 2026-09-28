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
