nome = str(input('Digite seu nome completo: ')).strip()
dividido = nome.split()

print('Seu nome é: {}.\nCom letras maiúsculas, fica {}.\nCom letras minúsculas, é {}.'.format(nome, nome.upper(), nome.lower()))
print('Possui {} letras, sem contar espaços.\nSeu primeiro nome tem {} letras. '.format(len(nome) - nome.count(' '), len(dividido[0])))
