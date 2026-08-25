def fatorial(num, show = False):
    '''
    -> Calcula o Fatorial de um número.
    :param num: O fatorial a ser calculado.
    :param show: [Opcional] Mostrar ou não a conta.
    :return: O valor do Fatorial de um número num.
    '''
    resp = 1
    for n in range(num, 1, -1):
        if show == True:
            print(f'{n} ',end='x ')
        resp *=n
    return print(f'1 = {resp}')
    
    
print('--'*20)
fatorial(5, show = True)
