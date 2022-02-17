# Exercício Python 73:
'''Crie uma tupla preenchida com os 20 primeiros colocados da Tabela
do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
a) Os 5 primeiros times.
b) Os últimos 4 colocados.
c) Times em ordem alfabética.
d) Em que posição está o time da Chapecoense.'''

times = ('Atlético MG', 'Flamengo', 'Palmeiras', 'Fortaleza', 'Corinthians',
         'Bragantino', 'Fluminense', 'América MG', 'Atlético GO', 'Santos',
         'Ceará', 'Internacional', 'São Paulo', 'Athlético PR', 'Cuiabá',
         'Juventude', 'Grêmio', 'Bahia', 'Sport', 'Chapecoense')
print('-='*20)
print(f'Os cinco primeiros times são: {times[:5]}')
print('-='*20)
print(f'Os quatro últimos colocados são: {times[-4:]}')
print('-='*20)
print(f'Times em ordem alfabética {sorted(times)}')
print('-='*20)
print(f'O Chapecoense está na {times.index("Chapecoense")+1}ª posição')
