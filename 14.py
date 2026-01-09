# Listas com pares e ímpares
valores = [[], []]
pares = 0
impares = 0
for v in range(1, 8):
    valor = (int(input(f'Digite o {v} valor: ')))
    if valor % 2 == 0:
        valores[0].append(valor)
    if valor % 2 == 1:
        valores[1].append(valor)
    
valores[1].sort()
valores[0].sort()
print(f'Os valores pares foram: {valores[0]}')
print(f'Os valores impares foram: {valores[1]}')