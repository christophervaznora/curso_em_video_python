print('-='*20)
print('Comparador de números')
print('-='*20)
num1 = float(input('Digite o primeiro número: '))
num2 = float(input('Digite o segundo número: '))
if num1 > num2:
    print('o primeiro valor é maior')
elif num2 > num1:
    print('o segundo valor é maior')
else:
    print('Os valores são iguais')
