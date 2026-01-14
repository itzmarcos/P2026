# Unindo dicionários e listas
dados = dict()
info = list()
while True:
    nome = (str(input('Nome: ')))
    info.append(nome)       
    while sexo not in 'MF':
        sexo = ' '
        sexo = (str(input('Sexo[M/F]: '))).strip().upper()[0]
        info.append(sexo)
    if sexo != 'MF':
        print('ERRO! Por favor, digite apenas M ou F.')