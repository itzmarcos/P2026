# Unindo dicionários e listas
dados = dict()
info = list()
while True:
    nome = (str(input('Nome: ')))
    info.append(nome)     
    sexo = ' '  
    while sexo not in 'MF':   
        sexo = (str(input('Sexo[M/F]: '))).strip().upper()[0]
    if sexo == 'MF':
        info.append(sexo)
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar: ')).strip().upper()[0]
    if resp == 'N':
        break
print(info)