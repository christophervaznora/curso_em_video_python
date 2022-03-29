'''Exercício Python 112:
Dentro do pacote utilidadesCeV que criamos no desafio 111, temos um módulo chamado dado.
Crie uma função chamada leiaDinheiro() que seja capaz de funcionar como a função imputa(),
mas com uma validação de dados para aceitar apenas valores que sejam monetários.'''

from utilidadesCeV import moeda
from utilidadesCeV import dados

valor = dados.leiadinheiro('Digite o valor R$ ')
moeda.resumo(valor, 10, 30)
