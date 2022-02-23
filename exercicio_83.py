# Exercício Python 83:
'''Crie um programa
onde o usuário digite uma expressão qualquer que use parênteses.
Seu aplicativo deverá analisar se a expressão passada está com os parênteses
abertos e fechados na ordem correta.'''

expressao = str(input('Digite a expressão: '))
pilha = []
for simbol in expressao:
    if simbol == '(':
        pilha.append('(')
    elif simbol == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('A expressão está correta')
else:
    print('A expressão está errada')
