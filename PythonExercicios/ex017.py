from math import hypot

oposto = float(input('Digite o valor do cateto oposto: '))
adjac = float(input('Digite o valor do cateto adjacente: '))

print('Com {} e {} temos hipotenusa {:.3f}.'.format(oposto, adjac, hypot(oposto,adjac)))
