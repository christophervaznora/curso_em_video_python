# Exercício Python 56:
# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
# No final do programa, mostre: a média de idade do grupo,
# qual é o nome do homem mais velho.
# quantas mulheres têm menos de 20 anos.

soma_idade = 0
media_idade = 0
maior_idade_homem = 0
nome_homem_velho = ''
total_mulher_20 = 0

for pessoa in range(1, 5):
    print(f'----- {pessoa}ª pessoa -----')
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()
    soma_idade += idade
    if pessoa == 1 and sexo in 'Mm':
        maior_idade_homem = idade
        nome_homem_velho = nome
    if sexo in 'Mm' and idade > maior_idade_homem:
        maior_idade_homem = idade
        nome_homem_velho = nome
    if sexo in 'Ff' and idade < 20:
        total_mulher_20 += 1
    
media_idade = soma_idade / 4
print(f'A média de idade do grupo é de {media_idade} anos')
print(f'O homem mais velho tem {maior_idade_homem} e se chama {nome_homem_velho}')
print(f'O total de mulheres com mais de 20 anos no grupo é: {total_mulher_20}')
