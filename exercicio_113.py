# Exercício Python 113:
'''Reescreva a função leiaInt() que fizemos no desafio 104,
incluindo agora a possibilidade da digitação de um número de tipo inválido.
Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade.'''


def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('ERRO! Digite um número inteiro')
            continue
        else:
            return n


def leiaFloat(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print('ERRO! Digite um número real')
            continue
        else:
            return n


# main
num_int = leiaInt('Digite um número: ')
print(f'Você digitou o número {num_int}')
num_float = leiaFloat('Digite um número real: ')
print(f'Você digitou o número {num_float}')
