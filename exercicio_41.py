from datetime import date
atual = date.today().year
nascimento = int(input('Informe o ano de nscimento do atleta: '))
idade = atual - nascimento
print('Quem nasceu em {} tem {} anos em {}'.format(nascimento, idade, atual))
if idade <= 9:
    print('A categoria do atleta é MIRIM!!')
elif 14 >= idade > 9:
    print('A categoria do atleta é INFANTIL!!')
elif 19 >= idade > 14:
    print(('A categoria do atleta é JÚNIOR!!'))
elif 25 >= idade >19:
    print('A categoria do atleta é SÊNIOR!!')
elif idade >25:
    print('A categoria do atleta é MASTER!!')
