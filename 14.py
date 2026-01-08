# Listas com pares e ímpares
valores = []
for v in range(1, 8):
    valor = (int(input(f'Digite o {v} valor: ')))
    valores.append(valor)
    if valor % 2 == 0:
        valores.append(valor)
    if valor % 2 == 1:
        valores.append(valor)


print(valores)