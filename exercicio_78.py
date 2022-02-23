# Exercício Python 78:
'''Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
No final, mostre qual foi o maior e o menor valor digitado,
e as suas respectivas posições na lista.'''

num = []
maior = menor = 0
for cont in range(0, 5):
    num.append(int(input(f'Digite um número para a posição {cont}: ')))
    if cont == 0:
        maior = menor = num[cont]
    else:
        if num[cont] > maior:
            maior = num[cont]
        if num[cont] < menor:
            menor = num[cont]
print(f'Os valores digitados foram {num}')
print(f'O maior valor digitado foi {maior} nas posições ', end='')
for i, v in enumerate(num):
    if v == maior:
        print(f'{i}...', end='')
print()
print(f'O menor valor digitado foi {menor} nas posições ', end='')
for i, v in enumerate(num):
    if v == menor:
        print(f'{i}...', end='')
print()
