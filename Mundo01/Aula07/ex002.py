num1 = int(input('Insira um número: '))
num2 = int(input('Insira outro número: '))
som = num1 + num2
mult = num1 * num2
div = num1 / num2
divInt = num1 // num2
exp = num1 ** num2
rest = num1 % num2

print('A soma é {}, o produto é {}, e a divisão é {:.3f}.'.format(som, mult, div), end=' ')
#{:.3f} é 3 casas decimais flutuantes! end ='' é o que colocar no final, se pula linha ou não.

print('A divisão inteira é {}, \n O resto é {} \n Potencializando temos {}'.format(divInt, rest, exp))
