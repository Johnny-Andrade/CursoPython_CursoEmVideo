num1 = float(input('Digite um número: '))
num2 = float(input('Digite outro número: '))
if num1 > num2:
    print('{} é maior que {}'.format(num1, num2))
elif num2 > num1:
    print('{} é menor que {}'.format(num1, num2))
else:
    print('{} é igual a {}'.format(num1, num2))
