# Exercício Python 88:
'''Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
O programa vai perguntar quantos jogos serão gerados
e vai sortear 6 números entre 1 e 60 para cada jogo,
cadastrando tudo em uma lista composta.'''

from random import sample
from time import sleep
print('-' * 30)
print('Gerador de jogos')
print('-' * 30)
jogos = list()
a = list()
n = int(input('Quantos jogos?: '))
for c in range(n):
    a = sorted(sample(range(1, 61), 6))
    jogos.append(a[:])
    a.clear()
    print(f'Jogo {c+1}: {jogos[c:]}')
    sleep(0.5)
