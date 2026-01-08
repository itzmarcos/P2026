# Lista composta e análise de dados

pessoas = []
dados = []
total = maior = menor = 0
while True:
    pessoas.append(str(input('Nome: ')))
    pessoas.append(int(input('Peso: ')))
    total += 1
    pessoas.append(dados[:])
    dados.clear()
    if pessoas[1] == 1:
        maior = menor = pessoas[1]
    else:
        if pessoas[1] > maior:
            maior = pessoas[1]
        if pessoas[1] < menor:
            menor = pessoas[1]

    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continua: ')).strip().upper()
    if resp == 'N':
        break

print(f'O total de pessoas cadastradas foram {total}')
print(f'O maior peso é de {maior}')