distancia = float(input('Digite a distância da sua viagem: '))
if distancia <= 200:
    valor = distancia * 0.5
    print('O valor da sua passagem é de R$ {:.2f}'.format(valor))
else:
    valor = distancia * 0.75
    print('O valor da sua passagem é de R$ {:.2f}'.format(valor))
