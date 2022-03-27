# Exercício Python 99:
'''Faça um programa que tenha uma função chamada maior(),
que receba vários parâmetros com valores inteiros.
Seu programa tem que analisar todos os valores
e dizer qual deles é o maior.'''

from time import sleep

def maior(* num):
    cont = maior = 0
    print('Analisando os valores')
    for v in num:
        print(f'{v} ', end='', flush=True)
        sleep(0.5)
        if cont == 0:
            maior = v
        else:
            if v > maior:
                maior = v
        cont += 1
    print()
    print(f'O maior valor informado foi {maior}')


# programa principal
maior(2, 9, 12, 100, 0)
