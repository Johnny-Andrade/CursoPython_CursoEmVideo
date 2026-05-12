from time import sleep
escolha = 6
print('=='*20)
print('Mini Computador')
print('=='*20)

val1 = int(input('Escolha o primeiro valor: '))
val2 = int(input('Escolha o segundo valor: '))
while escolha != '5':
    escolha = str(input('''
[ 1 ] Somar
[ 2 ] Multiplicar
[ 3 ] Verificar o maior
[ 4 ] Escolher novos números
[ 5 ] Sair do Programa
                                                
Escolha o que fazer: ''')).strip()[0]
    if escolha == '1':
        print('A soma entre {} e {} é \033[34m{}\033[m.'.format(val1, val2, val1+val2))
        sleep(2)
    elif escolha == '2':
        print('A multiplicação entre {} e {} é \033[34m{}\033[m.'.format(val1, val2, val1*val2))
        sleep(2)
    elif escolha == '3':
        maior = val1
        if val2 > val1:
            maior = val2
        if val1 != val2:
            print('O maior valor entre {} e {} é \033[34m{}\033[m.'.format(val1, val2, maior))
        else:
            print('Ambos valores são \033[34miguais\033[m.')
        sleep(2)
    elif escolha == '4':
        val1 = int(input('Escolha o primeiro valor: '))
        val2 = int(input('Escolha o segundo valor: '))
        sleep(1)
    elif escolha == '5':
        print('Adeus! Obrigado por nos escolher.')
        sleep(.5)
    else:
        print('\033[31m[Erro]\033[m Valor inválido! Escolha novamente.')
        sleep(1)
