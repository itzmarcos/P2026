# Extraindo dados de uma Lista.
cont = 0
lista = []
while True:
    lista.append(int(input('Digite um valor: ')))      
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continua: ')).strip().upper()
    if resp == 'N':
        break


lista.sort(reverse=True)
print(f'Voce digitou {len(lista)} elementos')
print(f'Os valores em ordem decrescente foram: {lista}')
if 5 in lista:
    print('O valor 5 faz parte da lista!')
else:
    print('O valor 5 não faz parte da lista!')