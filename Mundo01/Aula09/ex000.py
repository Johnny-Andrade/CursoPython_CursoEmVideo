frase = 'Curso em Vídeo Python'

print('\nTemos {} letras o minúscula na frase, dos caracteres 0 a 12.\nSe quiser saber, deo começa no caractere {}. '.format(frase.count('o',0,13), frase.find('deo')))

print('Dentro da frase existe a palavra Curso? {}...\n'.format('Curso' in frase))
print('Sabia que a frase tem {} caracteres?'.format(len(frase)))
print('Agora, vamos dar uma mudada na frase: {}'.format(frase))

print(frase.upper())
print(frase.lower())
print('Vale lembrar que \n{} é diferente de: \n{}'.format(frase.capitalize(), frase.title()))

frase2 = '   Aprenda Python  '
print('Vamos dar uma picotada na frase 2: \n{}'.format(frase2.strip()))
