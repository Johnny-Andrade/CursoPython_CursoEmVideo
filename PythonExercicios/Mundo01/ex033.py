print('Iniciando analisador de números!')
num1 = int(input('Digite um número: '))
num2 = int(input('Digite outro número: '))
num3 = int(input('Por fim, mais um número: '))
#Verificando o menor
menor = num1
if num2 < num1 and num2 < num3:
    menor = num2
if num3 < num1 and num3 < num2:
    menor = num3
#Verificando o maior
maior = num1
if num2 > num1 and num2 > num3:
    maior = num2
if num3 > num1 and num3 > num2:
    maior = num3
print('O menor número é {}'.format(menor))
print('O maior número é {}'.format(maior))
