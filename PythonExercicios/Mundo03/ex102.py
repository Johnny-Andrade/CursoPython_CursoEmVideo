def fatorial(num, show = False):
    '''
    -> Calcula o Fatorial de um número.
    :param num: O fatorial a ser calculado.
    :param show: [Opcional] Mostrar ou não a conta.
    :return: O valor do Fatorial de um número num.
    '''
    resp = 1
    for n in range(num, 0, -1):
        if show:
            print(n, end='')
            if n > 1:
                print(f' x ',end='')
            else:
                print(' = ',end='')
        resp *=n
    return print(f'{resp}')
    
    
print('--'*20)
fatorial(5, show = True)
