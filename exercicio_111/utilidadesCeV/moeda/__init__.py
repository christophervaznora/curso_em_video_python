def aumentar(preco=0, taxa=0, aparece=False):
    res = preco + (preco * taxa/100)
    return res if aparece is False else moeda(res)


def diminuir(preco=0, taxa=0, aparece=False):
    res = preco - (preco * taxa/100)
    return res if aparece is False else moeda(res)


def dobro(preco=0, aparece=False):
    res = preco * 2
    return res if aparece is False else moeda(res)


def metade(preco=0, aparece=False):
    res = preco / 2
    return res if aparece is False else moeda(res)


def moeda(preco=0, moeda='R$'):
    return f'{moeda}{preco:.2f}'.replace('.', ',')


def resumo(preco=0, aumento=10, reducao=10):
    print('=' * 40)
    print('Resumo'.center(40))
    print('=' * 40)
    print(f'Dobro do preço: \t\t\t{dobro(preco, True)}')
    print(f'Metade do preço: \t\t\t{metade(preco, True)}')
    print(f'Redução do preço em {reducao}%: \t{diminuir(preco, reducao, True)}')
    print(f'Aumento do preço em {aumento}%: \t{aumentar(preco, aumento, True)}')
