# Unindo dicionários e listas.
dados = dict()
info = list()
media = soma = 0
while True:
    dados.clear()
    dados['nome'] = str(input('Nome: '))
    while True:
        dados['sexo'] = str(input('Sexo[M/F]: ')).strip().upper()[0]   
        if  dados['sexo'] in 'MF':
            break
        print('Erro! Por favor digite apenas M ou F')
    dados['idade'] = int(input('Idade: '))
    soma += dados['idade']
    info.append(dados.copy())
    while True:
        resp = str(input('Quer continuar: ')).strip().upper()[0]
        if resp in 'SN':
            break
        print('Erro, responda apenas com S ou N')
    if resp == 'N':
        break
print(f'O grupo tem {len(info)} pessoas.')
media = soma / len(info)
print(f'A media entre as idade é {media:5.2f} anos')
print(f'As mulheres registrada foram ', end='')
for p in info:
    if p['sexo'] in 'Ff':
        print(f'{p["nome"]} ', end='')
print()
print('A lista das pessoas que estão acima da media: ', end='')
for p in info:
    if p['idade'] >= media:
        print()
        for k, v in p.items():
            print(f'{k} = {v} ', end='')
        print()
print('PROGRAMA FINALIZADO')