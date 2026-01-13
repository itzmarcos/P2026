# Dicionário em Python
dados = dict()
nota = []
dados['nome'] = str(input('Nome: '))
dados['media'] = float(input(f'Média de {dados["nome"]}: '))
if dados['media'] >= 7:
    dados['situacao'] = 'Aprovado'
elif dados['media'] <= 5.5:
    dados['situacao'] = 'Reprovado'
else:
    dados['situacao'] = 'Recuperaçao'

for k, v in dados.items():
    print(f'- {k} é igual a {v}')





