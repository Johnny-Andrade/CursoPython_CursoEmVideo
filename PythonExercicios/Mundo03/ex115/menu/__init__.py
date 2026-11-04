def linha(tam = 40):
    return print('-'*tam)


def cabeçalho(txt, tam = 40):
    linha()
    print(txt.center(tam))
    linha()


def leiaInt(msg):
    while True:
        try:
            n = int(input(msg).strip())
        except KeyboardInterrupt:
                    print('\n\033[31mO usuário preferiu não digitar esse número. Valor mudou para 0.\033[m')
                    return 3
        except:
            print('\033[31m[ERRO] Digite um número Inteiro válido.\033[m')
            continue
        else:
            return n


def interface(lista):
    from time import sleep
    while True:
        cabeçalho('MENU PRINCIPAL')
        c = 1
        for item in lista:
            print(f'\033[32m{c}\033[m - \033[34m{item}\033[m')
            c += 1
        linha()
        sleep(.3)
        opc = leiaInt('Sua opção: \033[32m')
        print('\033[m', end='')
        linha()
        if opc > len(lista):
            print('\033[31m[ERRO] Digite um número válido.\033[m')
            sleep(1.5)
        else:
            return opc

