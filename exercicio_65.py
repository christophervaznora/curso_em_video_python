# Exercício Python 65:
# Crie um programa que leia vários números inteiros pelo teclado.
# No final, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos.
# O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.
resposta = 'S'
media = soma = quantidade = maior = menor = 0
while resposta in 'Ss':
    numero = int(input('Digite um número: '))
    soma += numero
    quantidade += 1
    if quantidade == 1:
        maior = menor = numero
    else:
        if numero > maior:
            maior = numero
        if numero < menor:
            menor = numero
    resposta = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
media = soma / quantidade
print(f'Você digitou {quantidade} números e a média foi de {media}')
print(f'O maior número é {maior} e o menor é {menor}')
