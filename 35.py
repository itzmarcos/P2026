#
def lin(f):
    tam = len(f)
    print('-=' * tam)
while True:
    lin()
    print('SISTEMA DE AJUDA PyHELP')
    lin()
    f = str(input('funcao ou Biblioteca: '))
    lin()
    print(f'Acessando o manual {f}')
    lin()  
    if f == 'FIM':
        break
help(f)
lin()
print('Programa Finalizado..')