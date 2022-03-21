'''pessoas = {'nome': 'chris', 'sexo': 'M', 'idade': 22}
#print(f'O {pessoas["nome"]} tem [{pessoas["idade"]} anos')
print(pessoas.keys())
print(pessoas.values())
print(pessoas.items())
for k, v in pessoas.items():
    print(f'{k} = {v}')'''

# criando dicionários dentro de listas
'''brasil = []
estado_1 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
estado_2 = {'uf': 'São Paulo', 'sigla': 'SP'}
brasil.append(estado_1)
brasil.append(estado_2)
print(brasil)'''

# fatiamento em dicionários
estado = dict()
brasil = list()
for c in range(0, 3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do estado: '))
    brasil.append(estado.copy())
print(brasil)
for e in brasil:
    for k, v in e.items():
        print(f'O campo {k} tem valor {v}')
        