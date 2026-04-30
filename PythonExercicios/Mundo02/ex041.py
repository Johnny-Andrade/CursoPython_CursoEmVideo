from datetime import date
atual = date.today().year
ano = int(input('Digite seu ano de nascimento: '))
idade = atual - ano
print('Você tem {} anos, é um nadador '.format(idade), end='')
if idade <=9:
    print('\033[36mMIRIM\033[m.'.format(idade))
elif idade <=14:
    print('\033[34mINFANTIL\033[m.')
elif idade <=19:
    print('\033[33mJUNIOR\033[m.')
elif idade <= 25:
    print('\033[32mSÊNIOR\033[m.')
else:
    print('\033[31mMASTER\033[m.')
