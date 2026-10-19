def leiaInt(msg):
    while True:
        try:
            n = input(msg).strip()
            n = int(n)
            break
        except KeyboardInterrupt:
                    print('\n\033[31mO usuário preferiu não digitar esse número. Valor mudou para 0.\033[m')
                    n = 0
                    break
        except:
            print('\033[31m[ERRO] Digite um número Inteiro válido.\033[m')
    return n


def leiaFloat(msg):
    while True:
        try:
            n = input(msg).strip()
            n = float(n)
            break
        except KeyboardInterrupt:
            print('\n\033[31mO usuário preferiu não digitar esse número. Valor mudou para 0.\033[m')
            n = 0
            break
        except:
            print('\033[31m[ERRO] Digite um número Real válido.\033[m')
    return n


Nint = leiaInt('Digite um número Inteiro: ')
Nfloat = leiaFloat('Digite um número Real: ')
print(f'O valor Inteiro digitado foi {Nint} e o Real foi {Nfloat}')
