# Exercício Python 70:
'''Crie um programa que leia o nome e o preço de vários produtos.
O programa deverá perguntar se o usuário vai continuar ou não.
No final, mostre:
A) qual é o total gasto na compra.
B) quantos produtos custam mais de R$1000.
C) qual é o nome do produto mais barato.'''

total_gasto = 0
produto_mais_barato = 0
produto_acima_mil = 0
cont = 0
barato = ' '
while True:
    print('-'*20)
    produto = str(input('Nome do Produto: '))
    preco = float(input('Preço do produto R$ '))
    cont += 1
    total_gasto += preco
    if preco > 1000:
        produto_acima_mil += 1
    if cont == 1:
        produto_mais_barato = preco
        barato = produto
    else:
        if preco < produto_mais_barato:
            produto_mais_barato = preco
            barato = produto
    print('-'*20)
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if continuar == 'N':
        break
print('{:-^40}'.format(' FIM DO PROGRAMA '))
print(f'O total gasto foi de R${total_gasto:.2f}')
print(f'{produto_acima_mil} produtos custaram acima de R$1000,00 reais')
print(f'O produto mais barato foi {barato} e custou R${produto_mais_barato:.2f}')
