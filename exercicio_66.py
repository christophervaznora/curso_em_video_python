# Exercício Python 66:
'''Crie um programa que leia números inteiros pelo teclado.
O programa só vai parar quando o usuário digitar o valor 999.
No final, mostre quantos números foram digitados e a soma entre elas.'''

soma = cont = 0
while True:
    numero = int(input('Digite um número inteiro (999 para sair): '))
    if numero == 999:
        break
    soma += numero
    cont += 1
print(f'A soma dos valores é: {soma}')
print(f'Você digitou um total de {cont} números')
