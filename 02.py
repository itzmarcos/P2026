# Tuplas com Times de Futebol.

tabela = ('Flamengo', 'Palmeiras', 'Cruzeiro', 'Mirassol', 'Fluminense', 'Botafogo', 'Bahia', 'São Paulo', 'Gremio', 'Bragantino', 'Atletico-MG', 'Santos', 'Cotinthians', 'Vasco', 'Vitoria', 'Internacional', 'Ceara', 'Fortaleza', 'Juventude', 'Sport Recife')


print(f'Lista de times do Brasileirão: {tabela}')
print(f'Os 5 primeiro time são {tabela[0:5]}')
print(f'Os 4 ultimos são {tabela[-4:]}')
print(f'Times em ordem alfabética {sorted(tabela)}')
print(f'O São Paulo está na {tabela.index('São Paulo')+1} posição')
