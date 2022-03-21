# Exercício Python 93:
'''Crie um programa que gerencie o aproveitamento de um jogador de futebol.
O programa vai ler o nome do jogador e quantas partidas ele jogou.
Depois vai ler a quantidade de gols feitos em cada partida.
No final, tudo isso será guardado em um dicionário,
incluindo o total de gols feitos durante o campeonato.'''

jogador = {}
partidas = []
jogador['nome'] = str(input('Nome do jogador: '))
total = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
for c in range(0, total):
    partidas.append(int(input(f'Quantos gols na partida {c+1}: ')))
jogador['gols'] = partidas[:]
jogador['total'] = sum(partidas)
print('=' * 30)
print(jogador)
print('=' * 30)
for v, k in jogador.items():
    print(f'O campo {v} tem o valor {k}.')
print('=' * 30)
print(f'O jogador {jogador["nome"]} jogou {total} partidas.')
for i, v in enumerate(jogador["gols"]):
    print(f'   => Na partida {i+1} marcou {v} gols.')
if jogador["total"] == 0:
    print(f'O jogador {jogador["nome"]} não marcou gol.')
else:
    print(f'Foi um total de {jogador["total"]} gols.')
