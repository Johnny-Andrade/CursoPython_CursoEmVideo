larg = float(input('Diga a largura de uma parede em metros: '))
altu = float(input('Diga a altura da mesma parede em metros: '))
area = larg*altu

print('Esta parede tem a dimensão de {}x{}m, logo, temos {:.2f}m².'.format(larg, altu, area))
print('Como cada litro de tinta pinta 2m², precisaremos de {:.2f} litros!'.format(area/2))
