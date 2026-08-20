def contador(i, f, p):
    """
    -> Faz uma contagem e mostra na tela.
    :param i: início da contagem
    :param f: fim da contagem
    :param p: passo da contagem
    :return: sem retorno
    """
    c = i
    while c <= f:
        print(f'{c}', end='..')
        c += p
    print('FIM!')


def somar(a=0, b=0, c=0): #Caso não receba o valor, vai receber o valor opcional 0
    s = a + b + c
    return s

 
help(print)
print('-='*20)
print(input.__doc__)
print('-='*20)
help(contador)
print('-='*20)
r1 = somar(3,2,5)
r2 = somar(4,8)
r3 = somar(8)
print(f'Meus cálculos deram {r1}, {r2} e {r3}')
