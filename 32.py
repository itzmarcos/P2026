# Ficha do Jogador.

def jogador(n='<desconhecido>', g=0):
    
    print(f'O jogador {n} fez {g} gol(s) no campeonato.')

nome = str(input('Nome do jogador: ')).strip()
gol = str(input('Numero de gols: '))
if gol.isnumeric():
    gol = int(gol)
else:
    gol = 0
if nome.strip() == '':
    jogador(g=gol)
else:
    jogador(nome, gol)
