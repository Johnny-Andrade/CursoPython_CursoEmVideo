frase = str(input('Digite uma frase: ')).strip().upper()
print('A frase possui a letra A {} vezes, aparecendo pela primeira vez no {}° caractere.'.format(frase.count('A'), frase.find('A')+1))
print('Além disso, sua última aparição é no {}° caractere'.format(frase.rfind('A')+1))