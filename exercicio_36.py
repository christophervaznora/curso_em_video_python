print('-='*20)
print('Calculadora de financiamento')
print('-='*20)
casa = float(input('insira o valor da casa: R$'))
salario = float(input('Insira seu salário: R$'))
tempo = int(input('Em quantos anos deseja pagar:'))
prestacao = casa / (tempo * 12)
minimo = salario * 30 / 100
print('para pagar uma casa de R${:.2f} em {} anos'.format(casa, tempo), end= '')
print('A prestação será de R${:.2f}'.format(prestacao))
if prestacao <= minimo:
    print('Financiamento aprovado')
else:
    print('Empréstimo negado')
