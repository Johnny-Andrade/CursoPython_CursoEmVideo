print('-='*15)
print('{: ^30}'.format('Extensonador'))
print('-='*15)
tupla = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze', 'Catorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')
num = int(input('Digite um número de 0 a 20: '))
if num < 0 or num > 20:
    num = int(input('\033[31m[ERRO]\033[m Digite um número de 0 a 20: '))
print('A versão extensa desse número é: {}'.format(tupla[num]))
