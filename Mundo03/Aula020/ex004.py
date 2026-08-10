def soma(*vals):
    soma = 0
    for num in vals:
        soma += num
    print(f'A soma dos valores {vals} é igual a {soma}')


soma(5, 2)
soma(2, 9, 4)
