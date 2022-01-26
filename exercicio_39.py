from datetime import date
atual = date.today().year
nascimento = int(input('Informe seu ano de nascimento: '))
idade = atual - nascimento
print('Quem nasceu em {} tem {} anos em {}.'.format(nascimento, idade, atual))
if idade == 18:
    print('Você tem que se alistar IMEDIATAMENTE')
elif idade < 18:
    saldo = 18 - idade
    print('Ainda faltam {} anos para se alistar'.format(saldo))
    ano = atual + saldo
    print('Seu alistamento será em {}'.format(ano))
elif idade > 18:
    saldo = idade - 18
    print('Você deveria ter se aistado há {} anos'.format(saldo))
    ano = atual - saldo
    print('Seu alistamento foi em {}'.format(ano))
