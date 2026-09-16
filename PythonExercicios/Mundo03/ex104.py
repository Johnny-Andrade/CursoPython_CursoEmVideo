def leiaInt(txt):
    while True:
        num = str(input(txt)).strip()
        if num.isnumeric():
            valor = int(num)
            break
        else:
            print('\033[0;31m[ERRO] Digite um número inteiro válido.\033[m')
    return valor


n = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {n}.')
