preco = float(input('Preço das Compras: R$'))
print('''FORMAS DE PAGAMENTO
[ 1 ] À vista dinheiro
[ 2 ] À vista no cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')
opcao = int(input('Qual é a opção? '))
if opcao == 1:
    total = preco - (preco * 10 / 100)
elif opcao == 2:
    total = preco - (preco * 5 /100)
elif opcao == 3:
    total = preco
    parcela = total / 2
    print('Sua compra será parcelada em 2x de R${:.2f} SEM JUROS'.format(parcela))
elif opcao == 4:
    total = preco + (preco * 20 / 100)
    totparc = int(input('Informe o número de parcelas: '))
    parcela = total / totparc
    print('Sua compra será parcelada em {}x de R${:.2f} COM JUROS'.format(totparc,parcela))
else:
    total = 0
    print('OPÇÃO DE PAGAMENTO INVÁLIDA')
print('Sua compra de R${:.2f} vai custar R${:.2f} no final'.format(preco, total))
