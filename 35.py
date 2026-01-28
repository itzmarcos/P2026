#
from time import sleep
c = ('\033[m',
     '\033[0;30;41m', # 0 - sem cores
     '\33[0;30;42m',  # 1 - red
     '\33[0;30;43m',  # 2 - green
     '\33[0;30;43m',  # 3 - yellow
     '\33[0;30;44',)  # 4 - blue
def ajuda(com):
    titulo(f'Acessando o manual do comando \'{com}\'', 4)
    help(com)
    sleep(1)

def titulo(msg, cor=0):
    tam = len(msg) + 4
    print(c[cor], end='')
    print('~' * tam)
    print(f'  {msg}')
    print('~' * tam)
    print(c[0], end='')

comando = ''
while True:
    titulo('SISTEMA DE AJUDA PyHELP')
    comando = str(input("Funcao ou Biblioteca: "))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
titulo('ATE LOGO')