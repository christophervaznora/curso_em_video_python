# Exercício Python 94:
'''Crie um programa que leia nome, sexo e idade de várias pessoas,
guardando os dados de cada pessoa em um dicionário
e todos os dicionários em uma lista. No final, mostre:
A) Quantas pessoas foram cadastradas
B) A média de idade
C) Uma lista com as mulheres
D) Uma lista de pessoas com idade acima da média'''

pessoa = {}
dados = []
soma = media = 0
while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Nome: '))
    while True:
        pessoa['sexo'] = str(input('Sexo [M/F]: ')).upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('ERRO! digite apenas M ou F.')
    pessoa['idade'] = int(input('Idade: '))
    soma += pessoa['idade']
    dados.append(pessoa.copy())
    while True:
        resposta = str(input('Continuar? [S/N] ')).upper()[0]
        if resposta in 'SN':
            break
        print('ERRO! digite S/N')
    if resposta == 'N':
        break
print('=' * 30)
print(f'Ao todo temos {len(dados)} pessoas cadastradas')
media = soma / len(dados)
print(f'A média de idade é {media} anos')
print('As mulheres cadastradas foram ', end='')
for p in dados:
    if p['sexo'] == 'F':
        print(f'{p["nome"]} ', end='')
print()
print('Pessoas com idade acima da média: ', end='')
for p in dados:
    if p['idade'] >= media:
        print(f'{p["nome"]}', end='')
print()
