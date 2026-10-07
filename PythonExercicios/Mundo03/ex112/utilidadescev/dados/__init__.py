def leiaDinheiro(msg):
    valido = False
    while not valido:
        entrada = str(input(msg)).replace(',','.').strip()
        if entrada.isalpha() or entrada == '':
            print(f'\033[31m[ERRO]\033[m \"{entrada}\" é um preço inválido!')
        else:
            valido = True
            return float(entrada)


def leiaInt(txt):
    while True:
        num = str(input(txt)).strip()
        if num.isnumeric():
            valor = int(num)
            break
        else:
            print('\033[0;31m[ERRO] Digite um número inteiro válido.\033[m')
    return valor

