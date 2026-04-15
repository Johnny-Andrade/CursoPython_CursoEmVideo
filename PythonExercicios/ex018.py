from math import sin, cos, tan, radians

ang = float(input('Digite um ângulo em graus: '))
seno = sin(radians(ang))
cosseno = cos(radians(ang))
tangente = tan(radians(ang))

print('No ângulo de {}°, temos: \nSeno > {:.3f}\nCosseno > {:.3f}\nTangente > {:.3f}.'.format(ang, seno, cosseno, tangente))
