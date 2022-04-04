# Exercício Python 114:
'''Teste se o site pudim está acessível pelo computador usado.'''

import urllib
import urllib.request

try:
    site = urllib.request.urlopen('http://pudim.com.br')
except:
    print('Site não acessível no momento')
else:
    print('Tudo OK')
