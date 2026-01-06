valores = list()
while True:
    valores.append(int(input('Digite um valor: ')))
    print('Valor adiciona com sucesso...')
    if valores == valores:
        print('Valor duplicado! Não vou adicionar...')
    resp = ' '
    while resp not in "SN":
        resp = str(input('Quer continua: [S/N] ')).strip().upper()
    if resp == 'N':
        break
valores.sort()
print(f'Voce digitou os valores: {valores}')