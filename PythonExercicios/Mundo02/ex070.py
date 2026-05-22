total = caros = 0
barato = ''
print('=='*20)
print('LOJA CLAUDÃO BARATÃO')
print('=='*20)
while True:
    nome = str(input('\nDigite o nome do produto: ')).strip()
    preço = float(input('Digite o preço do produto: R$'))
    if barato == '':
        barato = nome
        prebarato = preço
    if preço > 1000:
        caros += 1
    total += preço
    if prebarato > preço:
        prebarato = preço
        barato = nome
    continuar = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]
    while continuar not in 'SsNn':
        continuar = str(input('\033[31m[ERRO]\033[m Deseja continuar? [S/N]: ')).strip().upper()[0]
    if continuar == 'N':
        break
print(f'\nNo total, você gastou R${total:.2f}.')
print(f'Tivemos {caros} produtos que custaram mais que R$1000.00')
print(f'Por fim, o produto mais barato foi {barato}, que custou R${prebarato:.2f}')
