print('-='*15)
print('{: ^30}'.format('Extensonador'))
print('-='*15)
tupla = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 
         'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 
         'Dez', 'Onze', 'Doze', 'Treze', 'Catorze', 
         'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 
         'Dezenove', 'Vinte')
num = int(input('Digite um número de 0 a 20: '))
while num < 0 or num > 20:
    num = int(input('\033[31m[ERRO]\033[m Digite um número de 0 a 20: '))
print(f'A versão extensa desse número é: {tupla[num]}')
