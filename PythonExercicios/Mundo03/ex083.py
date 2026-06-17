expressao = str(input('Digite a expressão: ')).strip()
parAberto = expressao.count('(')
parFechado = expressao.count(')')
if parAberto == 0 and parFechado == 0:
    print('Não há parênteses para analisar, reinicie o programa e tente novamente...')
elif parAberto > parFechado or parFechado > parAberto:
    print('Expressão inválida!')
else:
    print('Expressão válida!')
