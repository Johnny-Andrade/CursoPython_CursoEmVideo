def aumentar(n, perc=10):
    perc = (perc/100)+1
    return n*perc
    

def diminuir(n, perc=10):
    perc = 1-(perc/100)
    return n*perc
    

def dobro(n):
    res = n * 2
    return res


def metade(n):
    res = n / 2
    return res

