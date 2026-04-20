nome = input('Digite seu nome: ')
dividido = nome.split()

print('Seu nome completo é {}. \nSeu primeiro nome é {}. \nSeu último nome é {}.'.format(nome, dividido[0], dividido[len(dividido)-1]))
