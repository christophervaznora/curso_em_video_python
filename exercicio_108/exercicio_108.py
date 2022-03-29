'''Exercício Python 108:
Adapte o código do desafio #107,
criando uma função adicional chamada moeda()
que consiga mostrar os números como um valor monetário formatado.'''

import moeda

valor = float(input('Digite um valor R$ '))
print('=' * 30)
print(f'a metade de {moeda.moeda(valor)} é {moeda.moeda(moeda.metade(valor))} ')
print(f'o dobro de {moeda.moeda(valor)} é {moeda.moeda(moeda.dobro(valor))}')
print(f'aumentando 10% temos {moeda.moeda(moeda.aumentar(valor, 10))}')
print(f'diminuindo 30% temos {moeda.moeda(moeda.diminuir(valor, 30))}')
