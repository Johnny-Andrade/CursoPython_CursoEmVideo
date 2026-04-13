larg = float(input('Diga a largura de uma parede em metros: '))
altu = float(input('Diga a altura da mesma parede em metros: '))
area = larg*altu

print('Com uma largura de {}m, e uma altura de {}m, temos {}m².'.format(larg, altu, area))
print('Como cada litro de tinta pinta 2m², precisaremos de {} litros!'.format(area/2))
