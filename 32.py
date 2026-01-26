#


def jogador(gol=0, nome=0):
    nome = (input('Nome do jogador: '))
    gol = (input('Numero de Gols: '))
    if nome != str:
        nome = '<desconhecido>'
    print(f'O jogador {nome} fez {gol} gol(s) no campeonato.')

jogador()