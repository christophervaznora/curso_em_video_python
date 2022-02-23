# Exercício Python 79:
'''Crie um programa onde o usuário possa digitar vários valores numéricos
e cadastre-os em uma lista. Caso o número já exista lá dentro,
ele não será adicionado.No final, serão exibidos todos os valores
únicos digitados, em ordem crescente.'''

numeros = []
while True:
    n = int(input('Digite um valor: '))
    if n not in numeros:
        numeros.append(n)
    else:
        print('Valor já adicionado')
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if continuar == 'N':
        break
print(f'Os valores em ordem crescente são {sorted(numeros)}')
