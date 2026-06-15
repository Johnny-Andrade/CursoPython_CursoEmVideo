lista = []
while True:
    num = int(input('Digite um valor para a lista: '))
    if num not in lista:
        lista.append(num)
        print('Valor adicionado!')
    else:
        print('Valor duplicado. Não adicionado...')
    conf = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]
    if conf == 'N':
        break
print('-='*20)
print(f'Os valores digitados, em ordem crescente, são: {sorted(lista)}')
