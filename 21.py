# Cadastro de Trabalhador em Python
dados = dict()

dados['nome'] = str(input('Nome: '))
dados['ano'] = int(input('Ano de Nascimento: '))
dados['carteira'] = int(input('Carteira de Trabalho (0 não tem): '))
if dados['carteira'] != 0:
    dados['contrato'] = int(input('Ano de Contratação: '))
    dados['salario'] = int(input('Salario: '))


print(dados)