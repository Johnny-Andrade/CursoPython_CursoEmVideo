print('-='*20)
print('Termos de uma PA')
print('-='*20)
num = float(input('Digite o primeiro termo: '))
raz = float(input('Digite a razão: '))
cont = 1
termos = 10
nterm = 0
print('\nAbaixo, os 10 primeiros termos dessa PA:')
while termos != 0:
    while cont <= termos:
        print('{}'.format(num),end=' > ')
        num += raz
        cont += 1 
        nterm += 1
    print('Pausa!\n')
    cont = 1
    termos = int(input('[0 = Fim] Mais quantos termos?: '))
print('Progressão finalizada com {} termos!'.format(nterm))
