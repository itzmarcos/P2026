# Cadastro de Jogador de Futebol.
dados = dict()
gols = list()
soma = 0
dados['nome'] = str(input('Nome do jogador: '))
partidas = int(input(f'Quantas partidas {dados["nome"]} jogou: '))
dados['gols'] = gols
for p in range(0, partidas):
    gol = (int(input(f'Quantos gols na partida {p}: ')))
    soma += gol
    gols.append(gol)
    dados['total'] = soma    
print(dados)
for k, v in dados.items():
    print(f'O campo {k} tem o valor {v}')
print(f'O jogador {dados["nome"]} jogou {partidas} partidas.')
for p, g in enumerate(gols):
    print(f'=> Na partida {p}, fez {g} gols.')
print(f'Foi um total de {dados["total"]} gols')