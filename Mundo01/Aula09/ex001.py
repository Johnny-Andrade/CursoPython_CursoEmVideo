frase = 'Curso em Vídeo Python'
print('{} \n{} \n{} \n{}'.format(frase[3:13], frase[:9], frase[8:], frase[::2]))

print(frase.upper().count('O'))
print(frase.lower().find('vídeo'))

dividido = frase.split()
print(dividido[0])
print(dividido[2][3]) # Pega a terceira divisão ('Vídeo') e a quarta letra