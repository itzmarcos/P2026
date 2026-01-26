# Dividindo valores em várias listas.

lista = []
pares = []
impares = []
while True:
    valor = (int(input('Digite um numero: ')))
    lista.append(valor)
    if valor % 2 == 0:
        pares.append(valor)    
    if valor % 2 == 1:
        impares.append(valor)
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar: ')).strip().upper()
    if resp == 'N':
        break      
print(f'A lista completa é: {lista}')
print(f'A lista de pares é: {pares}')
print(f'A lista de impares é: {impares}')


# OUTRA SOLUÇÃO


# while True:
#     lista.append(int(input('Digite um numero: ')))
#     resp = str(input('Quer continua: '))
#     if resp in 'Nn':
#         break
# for i, v in enumerate(lista):
#     if v % 2 == 0:
#         pares.append(v)
#     elif v % 2 == 1:
#         impares.append(v)

# print(f'A lista completa é {lista}')
# print(f'A lista de pares é {pares}')
# print(f'A lista de impares é {impares}')