print('-='*20)
print('10 Primeiros termos de uma PA')
print('-='*20)
num = float(input('Digite o primeiro termo: '))
raz = float(input('Digite a razão: '))
cont = 0
while cont < 10:
    print('{}'.format(num),end=' > ')
    num += raz
    cont += 1 
print('Fim!')