# Exercício Python 64:
# Crie um programa que leia vários números inteiros pelo teclado.
# O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada.
# Mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).
numero = 0
cont = 0
soma = 0
numero = int(input('Digite um número [999 para parar]: '))
while numero != 999:
    soma += numero
    cont += 1
    numero = int(input('Digite um número [999 para parar]: '))
print(f'Você digitou {cont} e a soma entre eles foi de {soma}')
