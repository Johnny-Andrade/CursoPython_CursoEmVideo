palavras = ('Lembranças', 'Formula', 'Bolsa', 'Aperitivo', 'Comprimido', 'Adorno', 'Saudar', 'Primo', 'Lua', 'Refrescar', 'Curso', 'Video')
for item in palavras:
    print(f'Na palavra {item} temos ',end='')
    if (item.count('a') > 0) or (item.count('A') > 0):
        print('a ', end='')
    if (item.count('e') > 0) or (item.count('E') > 0):
        print('e ', end='')
    if (item.count('i') > 0) or (item.count('I') > 0):
        print('i ', end='')
    if (item.count('o') > 0) or (item.count('O') > 0):
        print('o ', end='')
    if (item.count('u') > 0) or (item.count('U') > 0):
        print('u ', end='')
    print()
