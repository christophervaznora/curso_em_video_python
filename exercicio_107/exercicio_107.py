# exercício 107:
'''Crie um módulo chamado moeda.py que tenha as funções:
aumentar(), diminuir(), dobro() e metade().
Faça também um programa que importe esse módulo e use algumas dessas funções.'''

import moeda

valor = float(input('Digite um valor R$ '))
print('=' * 30)
print(f'a metade do {valor} é {moeda.metade(valor)} ')
print(f'o dobro de {valor} é {moeda.dobro(valor)}')
print(f'aumentando 10% temos {moeda.aumentar(valor, 10)}')
print(f'diminuindo 30% temos {moeda.diminuir(valor, 30)}')
