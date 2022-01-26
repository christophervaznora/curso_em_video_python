from random import randint
computador = randint(0, 5)
print('Vou pensar em um número entre 0 e 5, tente advinhar...')
jogador = int(input('Em que número eu pensei? '))
if jogador == computador:
    print('Parabéns!! você acertou!!')
else:
    print('Que pena, você errou!! Eu pensei no número {} e não no número {}'.format(computador, jogador))
