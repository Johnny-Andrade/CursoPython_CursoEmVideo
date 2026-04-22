print('Iniciando analisador de números!')
num1 = int(input('Digite um número: '))
num2 = int(input('Digite outro número: '))
num3 = int(input('Por fim, mais um número: '))
maior = 0
menor = 0

if num1 > num2:
    maior = num1
    menor = num2
else:
    maior = num2
    menor = num1

if maior < num3:
    maior = num3

if menor > num3:
    menor = num3

print('O menor número é {}'.format(menor))
print('O maior número é {}'.format(maior))
