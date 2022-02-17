# Exercício Python 72:
'''Crie um programa que tenha uma dupla totalmente preenchida com uma contagem
por extenso, de zero até vinte.
Seu programa deverá ler um número pelo teclado (entre 0 e 20)
e mostrá-lo por extenso.'''

num = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete',
       'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'catorze', 'quinze',
       'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
while True:
    while True:
        leitura = int(input('Digite um número entre 0 e 20: '))
        if 0 <= leitura <= 20:
            break
        print('Tente novamente. ', end=' ')
    print(f'Você digitou o número {num[leitura]}')
    continuar = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if continuar == 'N':
        break
print('Programa encerrado!')
