# Exercício Python 102:
'''Crie um programa que tenha uma função fatorial()que receba dois parâmetros:
o primeiro que indique o número a calcular e outro chamado show,
que será um valor lógico (opcional) indicando se será mostrado ou não na tela
o processo de cálculo do fatorial.'''


def fatorial(num, show=False):
    """
    -> Calcula o fatorial de um número
    :param num: O número a ser calculado.
    :param show: (opcional) mostrar ou não o cálculo.
    """
    from math import factorial
    print(f'O fatorial de {num} é {factorial(num)}')
    if show is True:
        c = num
        f = 1
        while c > 0:
            print(f'{c}', end='')
            print(' x 'if c > 1 else ' = ', end='')
            f *= c
            c -= 1
        print(f'{f}')


# main program
fatorial(5, show=False)
