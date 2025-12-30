# Análise de dados em uma Tupla
cont = 0
a = int(input('Digite um numero: '))
b = int(input('Digite outro numero: '))
c = int(input('Digite mais um numero: '))
d = int(input('Digite o ultimo numero: '))
cont += 1
numeros = (a, b, c, d)
print(f'Voce digitou os valores {numeros}')
for pos, i in enumerate(numeros):
    print(f'O valor ')