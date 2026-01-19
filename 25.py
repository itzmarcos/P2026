# Função que calcula área
def area(lar, comp):
    resultado = lar * comp
    print(f'A área de um terreno de {lar} x {comp} é de {resultado}m²')


l = float(input('Largura(m): '))
c = float(input('Comprimento(m): '))

area(l, c)

