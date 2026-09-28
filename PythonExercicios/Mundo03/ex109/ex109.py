import moeda
p = float(input('Digite o preço: R$'))
print(f'\nA metade de {moeda.moeda(p)} é {moeda.metade(p, True)}')
print(f'O dobro de {moeda.moeda(p)} é {moeda.dobro(p, True)}')
print(f'Se houver um aumento de 10%, fica {moeda.aumentar(p, 10, True)}')
print(f'Se houver uma redução de 13%, fica {moeda.diminuir(p, 13, True)}')
