media = 0
mul20 = 0
hidade = 0
hvelho = ''
for pessoa in range(1,5):
    print('------ {}° PESSOA ------'.format(pessoa))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip().upper()
    somaidade += idade
    if sexo == 'F' and idade < 20:
        mul20 += 1
    if sexo == 'M' and idade > hidade:
        hidade = idade
        hvelho = nome
media = somaidade/4
print('A média de idade do grupo é {:.2f}'.format(media))
print('O homem mais velho do grupo tem {} anos e se chama {}'.format(hidade, hvelho))
print('Existem {} mulheres com menos de 20 anos.'.format(mul20))
