lista = []
while True:
    valor = int(input('Digite um número: '))
    lista.append(valor)
    confirm = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]
    while confirm not in 'SN':
        confirm = str(input('\033[31m[ERRO]\033[m Deseja continuar? [S/N]: ')).strip().upper()[0]
    if confirm == 'N':
        break
listaPar = []
listaImpar = []
for n in lista:
    if n % 2 == 0:
        listaPar.append(n)
    else:
        listaImpar.append(n)
print('-='*20)
print(f'\nA lista completa é: {lista}')
print(f'Uma lista de pares é: {listaPar}')
print(f'Uma lista de ímpares é: {listaImpar}')
