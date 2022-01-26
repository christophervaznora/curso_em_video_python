print('-='*20)
print('Calculadora de notas escolares')
print('-='*20)
n1 = float(input('Informe a primeira nota: '))
n2 = float(input('Informe a segunda nota: '))
media = (n1 + n2) / 2
print('Somanto as notas {:.1f} e {:.1f}, a média do aluno é: {:.1f}'.format(n1, n2, media))
if 7> media >= 5:
    print('O aluno está de RECUPERAÇÃO!! ')
elif media < 5:
    print('O aluno está REPROVADO!!')
else:
    print('O aluno está APROVADO!!')
