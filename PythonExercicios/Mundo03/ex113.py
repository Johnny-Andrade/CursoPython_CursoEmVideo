def leiaInt(msg):
    while True:
        try:
            n = int(input(msg).strip())
        except KeyboardInterrupt:
                    print('\n\033[31mO usuário preferiu não digitar esse número. Valor mudou para 0.\033[m')
                    return 0
        except:
            print('\033[31m[ERRO] Digite um número Inteiro válido.\033[m')
            continue
        else:
            return n


def leiaFloat(msg):
    while True:
        try:
            n = float(input(msg).strip().replace(',','.'))
            return n
        except KeyboardInterrupt:
            print('\n\033[31mO usuário preferiu não digitar esse número. Valor mudou para 0.\033[m')
            return 0
        except:
            print('\033[31m[ERRO] Digite um número Real válido.\033[m')


Nint = leiaInt('Digite um número Inteiro: ')
Nfloat = leiaFloat('Digite um número Real: ')
print(f'O valor Inteiro digitado foi {Nint} e o Real foi {Nfloat}')
