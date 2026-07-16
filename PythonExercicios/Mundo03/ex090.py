todos = dict()
while True:
    nome = str(input('Digite o nome do aluno: '))
    media = float(input('Digite a média do aluno: '))
    if media >= 7:
        situacao = 'Aprovado'
    elif media < 6:
        situacao = 'Reprovado'
