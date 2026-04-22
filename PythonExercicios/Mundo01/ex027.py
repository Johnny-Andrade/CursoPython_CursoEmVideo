nome = str(input('Digite seu nome: ')).strip()
dividido = nome.split()

print('\nMuito prazer em te conhecer!')
print('Seu primeiro nome é {}.'.format(dividido[0]))
print('Seu último nome é {}.\n'.format(dividido[len(dividido)-1]))
