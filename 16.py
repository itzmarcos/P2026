# MATRIZ.
par = col = maior = 0
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
        if matriz[l][c] % 2 == 0:
            par += matriz[l][c]
    print()
print(f'A soma dos valores pares é: {par}')
for l in range(0, 3):
    col += matriz[l][2]
print(f'A soma dos valores da coluna 3 é {col}')
for c in range(0, 3):
    if matriz[1][c] > maior:
        maior = matriz[1][c]
print(f'O maior numero digita na linha dois é: {maior}')