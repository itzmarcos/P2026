# Função de Contador

from time import sleep
# def contador(inicio, fim, passo):
#     print('Contagem de 1 até 10 de 1 em 1')
#     for c in range(0, 10, 1):      
#         print(f'{c+1}', end='', flush=True)
#     print('FIM')
#     print('Contagem de 10 até 0 de 2 em 2')
#     for c in range(10, -1, -2):       
#         print(f'{c}', end='', flush=True)
#     print('END')
#     print(f'Contagem de {inicio} até {fim} de {passo} em {passo} ')
#     for c in range(inicio, fim, passo):
#         print(f'{c}', end='', flush=True)
    


# inicio = int(input('Inicio: '))
# fim = int(input('Fim: '))
# passo = int(input('Passo: '))

# contador(incio, fim, passo)

def contador(i, f, p):
    if p < 0:
        p *= -1
    if p == 0:
        p = 1
    print(f'Contagem de {i} até {f} de {p} em {p}')
    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont} ', end='', flush=True)
            sleep(0.5)
            cont += p
        print('FIM')
    else:
        cont = i
        while cont >= f:
            print(f'{cont} ', end='', flush=True)
            sleep(0.5)
            cont -= p
        print('FIM')
      
contador(1, 10, 1)
contador(10, 0, 2)

inicio = int(input('Inicio: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
contador(inicio, fim, passo)