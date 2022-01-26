print('-='*20)
print('CALCULADORA DE IMC')
print('-='*20)
peso = float(input('Informe seu peso: '))
altura = float(input('Informe sua altura em m: '))
IMC = peso / (altura**2)
print('Seu IMC é: {:.1f}'.format(IMC))
if IMC < 18.5:
    print('Abaixo do Peso')
elif 18.5 <= IMC < 25:
    print('Peso Ideal')
elif 25 < IMC < 30:
    print('Sobrepreso')
elif 30 < IMC < 40:
    print('Obesidade')
else:
    print('Obesidade Mórbida')
