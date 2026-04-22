print('Dia de aumento!')
sal = float(input('Digite seu salário: R$'))
if sal <= 1250:
    novo = (sal*1.15)
else:
    novo = (sal*1.10)
print('Seu salário era R${:.2f}, o novo salário é R${:.2f}'.format(sal, novo))
