dados = {'nome': 'Pedro', 'idade': 25}
print(dados['nome'])
print(dados['idade'])
dados['sexo'] = 'M'
del dados['idade']
print(dados)
print('-='*20)
filme = {   'titulo': 'Star Wars',
            'ano': 1997,
            'diretor': 'George Lucas'
}
print(filme.values())
print(filme.keys())
print(filme.items())
for key, value in filme.items():
    print(f'O {key} é {value}!')
