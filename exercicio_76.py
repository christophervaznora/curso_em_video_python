# Exercício Python 76:
'''Crie um programa que tenha uma tupla única
com nomes de produtos e seus respectivos preços, na sequência.
No final, mostre uma listagem de preços,
organizando os dados em forma tabular.'''

produtos = ('Lápis', 1.75, 'Borracha', 2.00, 'Caderno', 8.99,
            'estojo', 5.99, 'Mochila', 119.99, 'Canetas', 13.75,
            'Compasso', 9.90, 'Transferidor', 4.99)
print('='*40)
print(f'{"LISTA DE PREÇOS":^40}')
print('='*40)
for pos in range(0, len(produtos)):
    if pos % 2 == 0:
        print(f'{produtos[pos]:.<30}', end='')
    else:
        print(f'R${produtos[pos]:>7.2f}')
