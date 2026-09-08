def sistema():
    while True:
        print('\033[34;42m')
        print('~~'*15)
        print(f'{"SISTEMA DE AJUDA PYHELP":^30}')
        print('~~'*15)
        print('\033[m')
        comando = str(input('Função ou Biblioteca > ')).strip()
        if comando == 'FIM':
            print('\033[41m')
            print('~~'*15)
            print(f'{"Até logo!":^30}')
            print('~~'*15)
            print('\033[m', end='')
            break
        else:
            print('\033[47m')
            help(comando)
            print('\033[m', end='')
    
    
sistema()