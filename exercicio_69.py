# Exercício Python 69:
'''Crie um programa que leia a idade e o sexo de várias pessoas.
A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar.
No final, mostre:
A) quantas pessoas tem mais de 18 anos.
B) quantos homens foram cadastrados.
C) quantas mulheres tem menos de 20 anos.'''

mais_dezoito = 0
homens = 0
mulher_menos_vinte = 0
print('-'*20)
print('Cadastro')
print('-'*20)
while True:
    idade = int(input('Digite a idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Informe o sexo [M/F]: ')).strip().upper()[0]
    if idade >= 18:
        mais_dezoito += 1
    if sexo == 'M':
        homens += 1
    if sexo == 'F' and idade < 20:
        mulher_menos_vinte += 1
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Deseja cadastrar outra pessoa? [S/N]: ')).strip().upper()[0]
    if continuar == 'N':
        break
print(f'Total de {mais_dezoito} pessoas com mais de 18 anos cadastradas')
print(f'total de {homens} homens cadastrados')
print(f'Total de {mulher_menos_vinte} mulheres com menos de 20 anos')
