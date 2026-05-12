'''from math import factorial
n = int(input('Digite um número para o fatorial: '))
f  = factorial(n)
print('O resultado de {}! é {}.'.format(n,f))'''
fatorial = int(input('Escolha um número para fazer o fatorial: '))
if fatorial < 0:
    print('[Fatorial inválido] Invertendo valor...')
    fatorial = fatorial * -1
etapa = fatorial
while etapa > 1:
    fatorial *= (etapa-1)
    etapa -= 1
print('O resultado é {}.'.format(fatorial))
