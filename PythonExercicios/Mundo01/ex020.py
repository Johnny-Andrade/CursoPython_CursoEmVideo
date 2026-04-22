from random import shuffle

nome1 = input('Primeiro aluno: ')
nome2 = input('Segundo aluno: ')
nome3 = input('Terceiro aluno: ')
nome4 = input('Por fim, o quarto aluno: ')
nomesLista = [nome1,nome2,nome3,nome4]

shuffle(nomesLista)
print('A ordem de alunos a aprensentar o trabalho é {}'.format(nomesLista))
