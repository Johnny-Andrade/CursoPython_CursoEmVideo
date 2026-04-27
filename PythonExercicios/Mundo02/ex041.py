from datetime import date
atual = date.today().year
ano = int(input('Digite seu ano de nascimento: '))
idade = atual - ano
if idade <=9:
    print('Você tem {} anos, é um nadador \033[36mMIRIM\033[m.'.format(idade))
elif idade <=14:
    print('Você tem {} anos, é um nadador \033[34mINFANTIL\033[m.'.format(idade))
elif idade <=19:
    print('Você tem {} anos, é um nadador \033[33mJUNIOR\033[m.'.format(idade))
elif idade == 20:
    print('Você tem 20 anos, é um nadador \033[32mSÊNIOR\033[m.')
else:
    print('Você tem {} anos, é um nadador \033[31mMASTER\033[m.'.format(idade))
