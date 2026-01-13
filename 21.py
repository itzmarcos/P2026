# Cadastro de Trabalhador em Python
from datetime import datetime
data = datetime.now().year
dados = dict()

dados['nome'] = str(input('Nome: '))
dados['idade'] = data - int(input('Ano de Nascimento: '))
dados['carteira'] = int(input('Carteira de Trabalho (0 não tem): '))
if dados['carteira'] != 0:
    dados['contrato'] = int(input('Ano de Contratação: '))
    dados['salario'] = int(input('Salario: R$'))
    dados['aposentadoria'] = dados['idade'] + 35

for k, v in dados.items():
    print(f'- {k} tem o valor {v}')