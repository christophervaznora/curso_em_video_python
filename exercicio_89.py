# Exercício Python 89:
'''Crie um programa que leia nome e duas notas de vários alunos
e guarde tudo em uma lista composta. No final, mostre um boletim
contendo a média de cada um e permita que o usuário possa mostrar as notas
de cada aluno individualmente.'''

ficha = []
while True:
    nome = str(input('Nome: '))
    nota_1 = float(input('Nota 1: '))
    nota_2 = float(input('Nota 2: '))
    media = (nota_1 + nota_2) / 2
    ficha.append([nome, [nota_1, nota_2], media])
    resposta = str(input('Quer continuar? [S/N] '))
    if resposta in 'Nn':
        break
print('=' * 30)
print(f'{"No.":<4}{"NOME":<10}{"MÉDIA":>8}')
print('=' * 30)
for i, a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
print('=' * 30)
while True:
    mostrar = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if mostrar == 999:
        break
    if mostrar <= len(ficha)-1:
        print(f'Notas de {ficha[mostrar][0]} são {ficha[mostrar][1]}')
print('FIM')
