# Exercício Python 96:
'''Faça um programa que tenha uma função chamada área(),
que receba as dimensões de um terreno retangular (largura e comprimento)
e mostre a área do terreno.'''

def area(larg, comp):
    a = larg * comp
    print(f'A área do terreno informado é de {a:.2f}m².')


print('-' * 20)
print('Calculadora de área')
print('-' * 20)
l = float(input('Informe comprimento(m): '))
c = float(input('Informe largura(m): '))
area(l, c)
