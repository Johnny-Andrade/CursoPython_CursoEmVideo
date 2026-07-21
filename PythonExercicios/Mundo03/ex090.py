nome = str(input('Nome: '))
media = float(input(f'Média de {nome}: '))
if media >= 7:
    situacao = 'Aprovado'
else:
    situacao = 'Reprovado'
aluno = {'Nome': nome, 'Média': media, 'Situação': situacao}
print('--'*20)
for item, valor in aluno.items():
    print(f'{item} é igual a {valor}')
