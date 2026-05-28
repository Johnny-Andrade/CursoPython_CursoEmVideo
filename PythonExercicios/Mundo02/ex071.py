print('=='*20)
print('Eletrônicos Danone')
print('=='*20)
cedula50 = cedula20 = cedula10 = cedula01 = 0
valor = int(input('\nQual valor você quer sacar? R$'))
while valor <= 0:
    valor = int(input('\033[31m[ERRO]\033[m Qual valor você quer sacar? R$'))
while True:
    if valor >= 50:
        cedula50 += 1
        valor -= 50
    elif valor >= 20:
        cedula20 += 1
        valor -= 20
    elif valor >= 10:
        cedula10 += 1
        valor -= 10
    elif valor >= 1:
        cedula01 += 1
        valor -= 1
        if valor == 0:
            break
print('Tivemos um Total de:')
if cedula50 > 0:
    print(f'{cedula50} cédulas de R$50.00')
if cedula20 > 0:
    print(f'{cedula20} cédulas de R$20.00')
if cedula10 > 0:
    print(f'{cedula10} cédulas de R$10.00')
if cedula01 > 0:
    print(f'{cedula01} cédulas de R$1.00')
print('Volte sempre!')
