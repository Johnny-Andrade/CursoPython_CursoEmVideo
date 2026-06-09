palavras = ('Lembranças', 'Formula', 'Bolsa', 'Aperitivo', 'Comprimido', 'Adorno', 'Saudar', 'Primo', 'Lua', 'Refrescar', 'Curso', 'Video')
for item in palavras:
    print(f'\nNa palavra {item} temos ',end='')
    for letra in item:
        if letra.lower() in 'aeiou':
            print(f'{letra} ', end='')
