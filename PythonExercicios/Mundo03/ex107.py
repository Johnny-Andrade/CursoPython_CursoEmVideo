import moeda
preco = float(input('Digite o preço: R$'))
print(f'\nA metade de R${preco} é R${moeda.metade(preco):.2f}')
print(f'O dobro de R${preco} é R${moeda.dobro(preco):.2f}')
print(f'Se houver um aumento de 10%, fica R${moeda.aumentar(preco):.2f}')
print(f'Se houver uma redução de 13%, fica R${moeda.diminuir(preco, 13):.2f}')
