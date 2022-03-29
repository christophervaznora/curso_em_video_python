def leiadinheiro(msg):
    valido = False
    while not valido:
        entrada = str(input(msg)).replace(',', '.').strip()
        if entrada.isalpha() or entrada == '':
            print('\033[0;31mEntrada inválida\033[m')
        else:
            valido - True
            return float(entrada)
