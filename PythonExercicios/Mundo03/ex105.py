def notas(*nota, sit = False):
    '''
    -> Função para analisar notas e situações de vários alunos.
    :param nota: Uma ou mais notas dos alunos (Várias são aceitas)
    :param sit: Valor opcional, indica se deve ou não adicionar a situação no dicionário.
    :return: dicionário com várias informações sobre as notas da turma dadas.
    '''
    resp = dict()
    resp["Total"] = len(nota)
    resp["Maior"] = max(nota)
    resp["Menor"] = min(nota)
    resp["Média"] = (sum(nota)/len(nota))
    if sit == True:
        if resp["Média"] >= 7:
            resp["Situação"] = "BOA"
        elif resp["Média"] >= 5:
            resp["Situação"] = "RAZOÁVEL"
        else:
            resp["Situação"] = "RUIM"
    return print(resp)
        

help(notas)
print('--'*20)
notas(5.5, 8, 4, 6.5, 9)
print()
