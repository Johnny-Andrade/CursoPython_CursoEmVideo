gen = 'b'
while (gen != 'M') and (gen != 'F') and (gen != 'NB'):
    gen = str(input('Digite seu gênero [M/F/NB]: ')).strip().upper()[0]
    if (gen != 'M') and (gen != 'F') and (gen != 'NB'):
        print('\033[31m[ERRO]\033[m Algo deu errado, digite novamente!')
print('Gênero {} registrado com sucesso.'.format(gen))
