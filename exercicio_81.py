# Exercício Python 81:
'''Crie um programa que vai ler vários números e colocar em uma lista.
Depois disso, mostre:
A) Quantos números foram digitados.
B) A lista de valores, ordenada de forma decrescente.
C) Se o valor 5 foi digitado e está ou não na lista.'''

lista = []
while True:
    lista.append(int(input('Digite um número: ')))
    resposta = str(int(input('Quer continuar? [S/N]: ')))
    if resposta in 'Nn':
        break
print(f'Foram digitados {len(lista)} números')
print(f'Os números em ordem decrescente são {sorted(lista, reverse=True)}')
if 5 in lista:
    print('O número 5 foi digitdo e está na lista')
else:
    print('O número 5 não foi digitado e não está na lista')
