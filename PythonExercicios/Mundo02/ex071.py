print('=='*20)
print('Eletrônicos Danone')
print('=='*20)
cedula50 = cedula20 = cedula10 = cedula1 = 0
valor = int(input('\nQual valor você quer sacar? R$'))
while valor > 50:
    cedula50 += 1
    valor -= 50
while valor > 20:
    cedula20 += 1
    valor -= 20
while valor > 10:
    cedula10 += 1
    valor -= 10
while valor >= 1:
    cedula1 += 1
    valor -= 1
    if valor == 0:
        break
print('Tivemos um Total de:')
print(f'{cedula50} cédulas de R$50.00')
print(f'{cedula20} cédulas de R$20.00')
print(f'{cedula10} cédulas de R$10.00')
print(f'{cedula1} cédulas de R$1.00')
print('Volte sempre!')
