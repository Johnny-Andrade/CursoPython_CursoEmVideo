print('Dia de aumento!')
sal = float(input('Digite seu salário: '))
if sal <= 1250:
    sal = (sal*1.15)
else:
    sal = (sal*1.10)
print('Seu novo salário é {:.2f}'.format(sal))
