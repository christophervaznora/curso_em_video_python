# Exercício Python 62:
# Melhorar DESAFIO 61, pergunte ao usuário se quer mostrar mais alguns termos.
# O programa encerrará quando ele disser que quer mostrar 0 termos.
primeiro = int(input('Primeiro Termo: '))
razao = int(input('Razão: '))
termo = primeiro
cont = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print(f'{termo} > ', end='')
        termo += razao
        cont += 1
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostrar a mais? '))
print('FIM')
