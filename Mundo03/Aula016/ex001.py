lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim')
# Tuplas são feitas com parênteses (até python 3.5), listas com colchetes, e dicionários com chaves
'''lanche[2] = 'Refrigerante' # Tuplas são imutáveis!
print(lanche)'''
for comida in lanche: # for comida in range(0,len(lanche)) também serve!
    print(f'Acabei de comer {comida}')
print(f'Nossa, comi muito! Foram {len(lanche)} coisas.')
print(sorted(lanche)) #para ordenar transformou em lista
