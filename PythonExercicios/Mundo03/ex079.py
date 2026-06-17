lista = list()
while True:
    num = int(input('Digite um valor para a lista: '))
    if num not in lista:
        lista.append(num)
        print('Valor adicionado!')
    else:
        print('Valor duplicado. Não adicionado...')
    confirm = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]
    while confirm not in 'SsNn':
        confirm = str(input('\033[31m[ERRO]\033[m Deseja continuar? [S/N]: ')).strip().upper()[0]
    if confirm in 'Nn':
        break
print('-='*20)
lista.sort()
print(f'Os valores digitados, em ordem crescente, são: {lista}')
