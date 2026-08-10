from time import sleep
def contagem(ini, fim, pas):
    print('-='*20)
    if pas == 0:
        print('\033[31m[ERRO]\033[m Passo impossível, retornando passo 1')
        pas = 1  
    if pas < 0:
            pas *= -1  
    print(f'Contagem de {ini} até {fim} de {pas} em {pas}')
    atual = ini
    if pas < 0:
        pas *= -1
    if fim > ini:
        while atual <= fim:
            print(f'{atual}', end=' ', flush= True)
            atual += pas
            sleep(.3)
        print('FIM!')
        sleep(1)
    if ini > fim:
        while atual >= fim:
            print(f'{atual}', end=' ', flush= True)
            atual -= pas
            sleep(.3)
        print('FIM!')
        sleep(1)


contagem(1, 10, 1)
contagem(10, 0, 2)
print('-='*20)
print('Agora é sua vez de personalizar a contagem!')
inici = int(input('Início: '))
final = int(input('Fim:    '))
passo = int(input('Passo:  '))
contagem(inici, final, passo)
