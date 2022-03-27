# Exercício Python 101:
'''Crie um programa que tenha uma função chamada voto()
que vai receber como parâmetro o ano de nascimento de uma pessoa,
retornando um valor literal indicando se uma pessoa tem voto
NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.'''


def voto(data):
    from datetime import datetime
    idade = datetime.now().year - ano
    if idade >= 70:
        return f'com {idade} anos, Voto opcional'
    elif idade >= 18:
        return f'com {idade} anos, voto obrigatório'
    elif 18 > idade > 16:
        return f'com {idade} anos, Voto opcional'
    else:
        return f'com {idade} anos, Voto negado'


# principal
ano = int(input('Ano de nascimento: '))
print(voto(ano))
