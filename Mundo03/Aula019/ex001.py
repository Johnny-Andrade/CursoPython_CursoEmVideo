pessoas = {'nome': 'Gustavo', 'sexo': 'M', 'idade': 22}
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos.\n')
for key in pessoas.keys():
    print(key)
print('-'*20)
for key in pessoas.values():
    print(key)  
print('-'*20) 
del pessoas['sexo']
pessoas['nome'] = 'Leandro'
pessoas['peso'] = 98.5
for key, value in pessoas.items():
    print(f'{key} = {value}')
