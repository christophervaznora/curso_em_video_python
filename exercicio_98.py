# Exercício Python 98:
'''Faça um programa que tenha uma função chamada contador(),
que receba três parâmetros: início, fim e passo.
Seu programa tem que realizar três contagens através da função criada:
a) de 1 até 10, de 1 em 1
b) de 10 até 0, de 2 em 2
c) uma contagem personalizada'''

from time import sleep


def contador(i, f, p):
    print(f'Contagem de {i} até {f} contando de {p} em {p}.')
    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont} ', end='', flush=True)
            sleep(0.5)
            cont += p
        print('FIM')
    else:
        if i > f:
            cont = i
            while cont >= f:
                print(f'{cont} ', end='', flush=True)
                sleep(0.5)
                cont -= p
            print('FIM')


# programa principal
contador(1, 10, 1)
contador(10, 0, 2)
print('+' * 30)
print('Contador personalizado')
print('+' * 30)
inicio = int(input('Início: '))
fim = int(input('Fim: '))
passo = abs(int(input('Passo: ')))
contador(inicio, fim, passo)
