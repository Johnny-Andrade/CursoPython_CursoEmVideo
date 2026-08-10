def area(larg, comp):
    tot = larg*comp
    print(f'A área de um terreno {larg}*{comp} é de {tot}m².')


print('Controle de Terrenos')
print('--'*15)
largura = float(input('LARGURA (m): '))
comprimento = float(input('COMPRIMENTO (m): '))
area(largura, comprimento)
