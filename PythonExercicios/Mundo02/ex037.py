print('-='*20)
print('Conversor de números')
print('-='*20)
num = int(input('Escreva um número inteiro qualquer: '))
print('--'*20)
conversao = int(input('[ 1 ] para Binário\n[ 2 ] para Octal e \n[ 3 ] para Hexadecimal\nEscolha: '))
if conversao == 1:
    print('{} convertido para BINÁRIO é igual a {}'.format(num, bin(num)[2:]))
elif conversao == 2:
    print('{} convertido para OCTAL é igual a {}'.format(num, oct(num)[2:]))
elif conversao == 3:
    print('{} convertido para HEXADECIMAL é igual a {}'.format(num, hex(num)[2:]))
else:
    print('\033[31m[ERRO]\033[m Reinicie o programa e digite corretamente.')
