# Exercício Python 54:
'''Crie um programa que leia o ano de nascimento de sete pessoas.
# No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.'''

from datetime import date
atual = date.today().year
total_maior = 0
total_menor = 0

for c in range(1, 8):
    nascimento = int(input(f'Digite o ano de nascimento da {c}ª pessoa: '))
    idade = atual - nascimento
    if idade >= 18:
        total_maior += 1
    else:
        total_menor += 1
print(f'Ao todo tivemos {total_maior} pessoas maiores de idade')
print(f'Ao todo tivemos {total_menor} pessoas menores de idade')
