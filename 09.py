# Lista ordenada sem repetições.

valores = list()
for v in range(0, 3):
    valor = int(input('Digite um valor: '))
    if v == 0 or valor > valores[-1]:
        valores.append(valor)
        print('Adicionado no final da lista')
    else:
        pos = 0
        while pos < len(valores):
            if valor <= valores[pos]:
                valores.insert(pos, valor)
                print(f'Adicionado na posição {pos} da lista')
                break
            pos += 1
print(f'Os valores digitados foram: {valores}')