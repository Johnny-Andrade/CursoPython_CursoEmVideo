print('=='*20)
print('Os 10 primeiros termos de uma P.A.')
print('=='*20)
num = float(input('Digite o primeiro termo da Progressão Aritmética: '))
raz = float(input('Digite a razão da PA: '))
for c in range(0,10):
    print('{}'.format(num), end=' -> ')
    num += raz
print('FIM!')
