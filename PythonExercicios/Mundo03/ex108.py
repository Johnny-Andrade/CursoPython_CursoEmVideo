import moeda
p = float(input('Digite o preço: R$'))
print(f'\nA metade de {moeda.moeda(p)} é {moeda.moeda(moeda.metade(p))}')
print(f'O dobro de {moeda.moeda(p)} é {moeda.moeda(moeda.dobro(p))}')
print(f'Se houver um aumento de 10%, fica {moeda.moeda(moeda.aumentar(p))}')
print(f'Se houver uma redução de 13%, fica {moeda.moeda(moeda.diminuir(p, 13))}')
