# Cadastro de Jogador de Futebol
dados = dict()
gols = list()

dados['nome'] = str(input('Nome do jogador: '))
partidas = int(input(f'Quantas partidas {dados["nome"]} jogou: '))
for p in range(0, partidas):
    dados['gols'] = int(input(f'Quantos gols na partida {p}: '))
    gols.append(dados['gols'])

print(gols)