'''Exercício Python 109:
Modifique as funções que form criadas no desafio 107
para que elas aceitem um parâmetro a mais,
informando se o valor retornado por elas vai ser ou não
formatado pela função moeda(), desenvolvida no desafio 108.'''

import moeda

valor = float(input('Digite um valor R$ '))
print('=' * 30)
print(f'a metade de {moeda.moeda(valor)} é {moeda.metade(valor, True)} ')
print(f'o dobro de {moeda.moeda(valor)} é {moeda.dobro(valor, True)}')
print(f'aumentando 10% temos {moeda.aumentar(valor, 10, True)}')
print(f'diminuindo 30% temos {moeda.diminuir(valor, 30, True)}')
