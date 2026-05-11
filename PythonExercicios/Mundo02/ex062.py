print('-='*20)
print('Termos de uma PA')
print('-='*20)
num = float(input('Digite o primeiro termo: '))
raz = float(input('Digite a razão: '))
cont = 1
termos = 10
print('\nAbaixo, os 10 primeiros termos dessa PA:')
while termos != 0:
    while cont <= termos:
        print('{}'.format(num),end=' > ')
        num += raz
        cont += 1 
    print('Fim!\n')
    cont = 1
    termos = int(input('[0 Finaliza] Mais quantos termos?: '))
