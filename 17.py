# Palpites para a Mega Sena
import random
from random import randint
from time import sleep
# jogo = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15,
#         16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30,
#         31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45,
#         46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60]
# valor = int(input('Quantos jogos você quer que eu sorteie: '))
# print(f'------- SORTEANDO {valor} JOGOS-------')
# for c in range(1, valor+1):
#     sleep(0.5)
#     sorteio = random.sample(jogo, 6)
    
#     print(f'Jogo {c}: {sorteio}')
# print('------------BOA SORTE------------')


# OUTRA FORMA

lista = list()
jogos = list()

quant = int(input('Quantos jogos voce quer que eu sorteie: '))
tot = 1
while tot <= quant:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1
print(f'-------- SORTEANDO {quant} JOGOS -------')
for i, l in enumerate(jogos):
    print(f'Jogo {i+1}: {l}')
    sleep(0.5)
print('--------- BOA SORTE --------------')