valores = []
for n in range(0,5):
    valores.append(int(input(f'Digite um número para a posição {n}: ')))
maior = max(valores)
menor = min(valores)
posMaior = []
posMenor = []
anteMaior = anteMenor = 0
for numMaior in range (0, valores.count(maior)):
    posMaior.append(valores.index(maior, anteMaior+1))
    anteMaior += valores.index(maior)
for numMenor in range (0, valores.count(menor)):
    posMenor.append(valores.index(menor, anteMenor+1))
    anteMenor += valores.index(menor)
print('-='*10)
print(f'Você digitou os valores {valores}')
print(f'O maior valor é {maior}, que está nas posições {posMaior}')
print(f'O menor valor é {menor}, que está nas posições {posMenor}')
