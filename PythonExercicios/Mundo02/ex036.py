print('-='*20)
print('Analisador de Compra de casa')
print('-='*20)
casa = float(input('Digite o valor da casa. R$'))
sal = float(input('Digite seu salário. R$'))
anos = int(input('Digite em quantos anos você pretende pagar: '))
prestacao = casa/(anos*12)
print('Para pagar, você terá que fazer \033[35m{}\033[m prestações de \033[34mR${:.2f}\033[m'.format(anos*12, prestacao))
if prestacao > (sal*0.3):
    print('Empréstimo \033[31mnegado\033[m, o valor excede 30% do seu salário atual!')
else:
    print('Você foi \033[32mautorizado\033[m a comprar! Boa sorte em sua nova casa.')
