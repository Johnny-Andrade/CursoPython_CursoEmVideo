cidade = str(input('Digite o nome de uma cidade: ')).strip()
print('A cidade {} tem Santo em qualquer lugar? {}!'.format(cidade, 'SANTO' in cidade.upper()))
print('A cidade {} começa com Santo? {}!'.format(cidade, cidade[:5].upper() == 'SANTO'))
