# Lista composta e análise de dados.

pessoas = []
dados = []
maior = menor = 0
while True:
    pessoas.append(str(input('Nome: ')))
    pessoas.append(float(input('Peso: ')))
    if len(dados) == 0:
        maior = menor = pessoas[1]
    else:
        if pessoas[1] > maior:
            maior = pessoas[1]
        if pessoas[1] < menor:
            menor = pessoas[1]
    dados.append(pessoas[:])
    pessoas.clear()
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continua: ')).strip().upper()[0]
    if resp == 'N':
        break
print(f'O total de pessoas cadastradas foram {len(dados)}.')
print(f'O maior peso foi {maior}KG', end=' ')
for p in dados:
    if p[1] == maior:
        print(f'{p[0]}', end=' ')
print()
print(f'O menor peso foi {menor}KG', end=' ')
for p in dados:
    if p[1] == menor:
        print(f'{p[0]}', end=' ')
print()