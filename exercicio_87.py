# Exercício Python 87:
'''Aprimore o desafio anterior, mostrando no final:
A) A soma de todos os valores pares digitados.
B) A soma dos valores da terceira coluna.
C) O maior valor da segunda linha.'''

soma_par = soma_terceira = maior_segunda = 0
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
        if matriz[l][c] % 2 == 0:
            soma_par += matriz[l][c]
    print()
print(f'A soma dos valores pares é {soma_par}.')
for l in range(0, 3):
    soma_terceira += matriz[l][2]
print(f'A soma dos valores da terceira coluna é {soma_terceira}.')
for c in range(0, 3):
    if c == 0 or matriz[1][c] > maior_segunda:
        maior_segunda = matriz[1][c]
print(f'O maior valor da segunda linha é {maior_segunda}.')
