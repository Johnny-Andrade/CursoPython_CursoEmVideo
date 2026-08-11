def escreva(txt):
    tamanho = len(txt) + 4
    print('~'*tamanho)
    print(f'  {txt}')
    print('~'*tamanho)


escreva('Gustavo Guanabara')
escreva('Curso de Python no YouTube')
escreva('CeV')
print('-='*20)
escreva(str(input('Digite algo: ')).strip())
