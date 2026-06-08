from time import sleep
print('-='*15)
print('{: ^30}'.format('Menu Brasileirão'))
print('-='*15)
tabela = ('Palmeiras', 'Flamengo', 'Fluminense', 'Athletico-PR', 
          'Bragantino', 'Bahia', 'Coritiba', 'São Paulo', 
          'Atlético-MG', 'Corinthians', 'Cruzeiro', 'Botafogo', 
          'EC Vitória', 'Internacional', 'Santos', 'Grêmio', 
          'Vasco da Gama', 'Remo', 'Mirassol', 'Chapecoense')
while True:
    print('--'*15)
    print('A) 5 Primeiros Colocados')
    print('B) 4 Últimos Colocados')
    print('C) Top 20 em Ordem Alfabética')
    print('D) Posição do Chapecoense')
    print('E) Fechar programa.')
    print('--'*15)
    menu = str(input('Digite a Opção Escolhida: ')).strip().upper()[0]
    while menu not in 'ABCDE':
        menu = str(input('\033[31m[ERRO]\033[m Digite a Opção Escolhida: ')).strip().upper()[0]
    if menu == 'A':
        print(f'Os cinco primeiros colocados são: {tabela[:5]}')
        sleep(1)
    elif menu == 'B':
        print(f'Os quatro último são: {tabela[-4:]}')
        sleep(1)
    elif menu == 'C':
        print(sorted(tabela))
        sleep(1)
    elif menu == 'D':
        print(f'O chapecoense está na {tabela.index("Chapecoense")+1}° Posição')
        sleep(1)
    elif menu == 'E':
        break
print('Muito obrigado por usar nosso programa!')
