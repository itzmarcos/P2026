#
from time import sleep
def contador(inicio, fim, passo):
    print('Contagem de 1 até 10 de 1 em 1')
    for c in range(0, 10, 1):      
        print(f'{c}', end=' ')
    print('FIM')
    print('Contagem de 10 até 0 de 2 em 2')
    for c in range(10, 0, -2):       
        print(f'{c}', end=' ')
    print('END')
    print(f'Contagem de {incio} até {fim} de {passo} em {passo} ')
    for c in range(inicio, fim, passo):
        print(f'{c}', end=' ')


incio = int(input('Inicio: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))

contador(incio, fim, passo)
