palavras = ('Lembranças', 'Fórmula', 'Bolsa', 'Aperitivo', 'Comprimido', 'Adorno', 'Saudar', 'Primo', 'Lua', 'Refrescar', 'Curso', 'Vídeo')
for item in palavras:
    print(f'\nNa palavra {item} temos ',end='')
    for letra in item:
        if letra.lower() in 'aáãâeéêiíîoóôõuúû':
            print(f'{letra.lower()} ', end='')
