# Aprimorando os Dicionários
jogadores = dict()
lista = list()
while True:
    jogadores['nome'] = str(input('Nome do jogador: '))
    partidas = int(input(f'Quantas partidas {jogadores["nome"]} jogou: '))
    for p in range(0, partidas):
        gol = int(input(f'Quantos gols na partida {p}: '))
    while True:
        resp = str(input('Quer continuar: ')).upper()[0]
        if resp in 'Nn':
            break