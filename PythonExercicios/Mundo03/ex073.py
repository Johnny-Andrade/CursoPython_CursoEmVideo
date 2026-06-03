print('-='*15)
print('{: ^30}'.format('Menu Brasileirão'))
print('-='*15)
tabela = ('Palmeiras', 'Flamengo', 'Fluminense', 'Athletico-PR', 'Bragantino', 'Bahia', 'Coritiba', 'São Paulo', 'Atlético-MG', 'Corinthians', 'Cruzeiro', 'Botafogo', 'EC Vitória', 'Internacional', 'Santos', 'Grêmio', 'Vasco da Gama', 'Remo', 'Mirassol', 'Chapecoense')
print('''------------------------------
A) 5 Primeiros Colocados
B) 4 Últimos Colocados
C) Top 20 em Ordem Alfabética
D) Posição do Chapecoense
------------------------------''')
menu = str(input('Digite a Opção Escolhida: ')).strip().upper()[0]
while menu not in 'ABCD':
    menu = str(input('\033[31m[ERRO]\033[m Digite a Opção Escolhida: ')).strip().upper()[0]
if menu == 'A':
    print('Os cinco primeiros colocados são: {}'.format(tabela[:5]))
elif menu == 'B':
    print('Os quatro último são: {}'.format(tabela[-4:]))
elif menu == 'C':
    print(sorted(tabela))
elif menu == 'D':
    print('O chapecoense está na {}° Posição'.format(tabela.index('Chapecoense')+1))
