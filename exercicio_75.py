# Exercício Python 75:
'''Desenvolva um programa que leia quatro valores pelo teclado
e guarde-os em uma tupla. No final, mostre:
A) Quantas vezes apareceu o valor 9.
B) Em que posição foi digitado o primeiro valor 3.
C) Quais foram os números pares.'''

num = (int(input('Digite um número: ')),
       int(input('Digite um segundo número: ')),
       int(input('Digite um terceiro número: ')),
       int(input('Digite um quarto número: ')))
print(f'O número 9 aparece {num.count(9)} vezes')
if 3 in num:
    print(f'O número 3 aparece na {num.index(3)+1}ª posição')
else:
    print('O número 3 não aparece nenhuma vezes')
print('Os valores pares digitados foram ', end=' ')
for n in num:
    if n % 2 == 0:
        print(n, end=' ')
