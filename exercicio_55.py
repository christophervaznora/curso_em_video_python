# Exercício Python 55: Faça um programa que leia o peso de cinco pessoas.
# No final, mostre qual foi o maior e o menor peso lidos.

for c in range(1, 6):
    peso = float(input(f'Digite o peso da {c}ª pessoa: '))
    if c == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print(f'O maior peso é {maior}kg')
print(f'O menor peso é {menor}kg')
