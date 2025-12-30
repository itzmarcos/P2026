# Maior e menor valores em Tupla
from random import randint
# maior = menor = 0

# for i in range(5):
#     numero = random.randint(1, 10)
#     print(numero, end=' ')
#     if i == 1:
#         maior = menor = numero
#     else:
#         if numero > maior:
#             maior = numero
#         if numero < menor:
#             menor = numero

# print(f'O maior numero sorteado foi {maior} e o menor foi {menor}')

# REVISAO!
numeros = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
print('Os valores sorteados foram: ', end= ' ')
for i in numeros:
    print(f'{i}', end=' ')
print(f'\nO maior valor sorteado foi {max(numeros)}')
print(f'O menor valor sorteado foi {min(numeros)}')
