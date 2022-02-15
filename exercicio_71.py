# Exercício Python 71:
'''Crie um programa que simule o funcionamento de um caixa eletrônico.
No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro)
e o programa vai informar quantas cédulas de cada valor serão entregues.
OBS:
considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.'''

valor = int(input('Informe o valor de saque R$ '))
total_saque = valor
cedula_maior = 50
total_cedula = 0
while True:
    if total_saque >= cedula_maior:
        total_saque -= cedula_maior
        total_cedula += 1
    else:
        if total_cedula > 0:
            print(f'Total de {total_cedula} cédulas de R${cedula_maior}')
        if cedula_maior == 50:
            cedula_maior = 20
        elif cedula_maior == 20:
            cedula_maior = 10
        elif cedula_maior == 10:
            cedula_maior = 1
        total_cedula = 0
        if total_saque == 0:
            break
