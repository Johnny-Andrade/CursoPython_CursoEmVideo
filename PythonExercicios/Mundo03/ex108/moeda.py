def aumentar(n=0, perc=10):
    perc = (perc/100)+1
    return n*perc
    

def diminuir(n=0, perc=10):
    perc = 1-(perc/100)
    return n*perc
    

def dobro(n=0):
    res = n * 2
    return res


def metade(n=0):
    res = n / 2
    return res

def moeda(n, moeda='R$'):
    return f'{moeda}{n:.2f}'.replace('.',',')

