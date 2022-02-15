# Exercício Python 59:
'''Crie um programa que leia dois valores e mostre um menu na tela:
    [ 1 ] somar
    [ 2 ] multiplicar
    [ 3 ] maior
    [ 4 ] novos números
    [ 5 ] sair do programa
Seu programa deverá realizar a operação solicitada em cada caso.'''

num_1 = int(input('Digite o primeiro número: '))
num_2 = int(input('Digite o segundo número: '))
escolha = 0
while escolha != 5:
    print('''Selecione a operação desejada:
    [ 1 ] somar
    [ 2 ] multiplicar
    [ 3 ] maior
    [ 4 ] novos números
    [ 5 ] sair do programa''')
    escolha = int(input('Digite sua opção: '))
    if escolha == 1:
        soma = num_1 + num_2
        print(f'A soma de {num_1} e {num_2} é {soma}')
    elif escolha == 2:
        multiplicar = num_1 * num_2
        print(f'A multiplicação de {num_1} e {num_2} é {multiplicar}')
    elif escolha == 3:
        if num_1 > num_2:
            print(f'{num_1} é maior')
        elif num_2 > num_1:
            print(f'{num_2} é maior')
        else:
            print('Os dois são iguais')
    elif escolha == 4:
        print('Informe os números novamente:')
        num_1 = int(input('Primeiro número: '))
        num_2 = int(input('Segundo número: '))
    else:
        print('Opção inválida! Tente novamente')
    print('=-='*20)
print('Fim do programa')
