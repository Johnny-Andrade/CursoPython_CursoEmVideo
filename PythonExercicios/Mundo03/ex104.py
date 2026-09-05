def leiaInt(txt):
    num = input(txt)
    while True:
        if num in '0123456789' and len(num) >= 1:
            break
        else:
            print('\033[31m[ERRO] Digite um número inteiro válido.\033[m')
            num = input(txt)
    return num


n = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {n}.')
