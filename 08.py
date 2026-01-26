# Valores únicos em uma Lista.

valores = list()
while True:
    valor = int(input('Digite um valor: '))
    
    if valor not in valores:
        valores.append(valor)
        print('Valor adiciona com sucesso...')
    else:
        print('Valor duplicado! Não vou adicionar...')
    resp = ' '
    while resp not in "SN":
        resp = str(input('Quer continua: [S/N] ')).strip().upper()
    if resp == 'N':
        break
valores.sort()
print(f'Voce digitou os valores: {valores}')