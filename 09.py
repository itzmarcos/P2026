# Lista ordenada sem repetições

valores = list()

for v in range(3):
    valor = int(input('Digite um valor: '))
    if valor in valores:
        valores.append(valor)
        print('Adicionado no final da lista!')





valores.sort()
print(f'Os valores digitados foram: {valores}')