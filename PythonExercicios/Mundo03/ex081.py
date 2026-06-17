lista = []
while True:
    valor = int(input('Digite um valor: '))
    lista.append(valor)
    confirm = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]
    while confirm not in 'SN':
        confirm = str(input('\033[31m[ERRO]\033[m Deseja continuar? [S/N]: ')).strip().upper()[0]
    if confirm == 'N':
        break
lista.sort(reverse = True)
print('-='*20)
print(f'Você digitou {len(lista)} números!')
print(f'A lista, de forma decrescente, é: {lista}')
if 5 in lista:
    print('O número 5 está presente na lista!')
else:
    print('Não há número 5 na lista...')
