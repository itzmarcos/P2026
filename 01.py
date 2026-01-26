# Número por Extenso.

cont = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez')

while True:
    numero = int(input('Digite um numero entre 0 e 10: '))
    while numero > 10:
        numero = int(input('Voce digitou errado, tente novamente: '))
    if 0 <= numero <= 10:
        print(f'Voce digitou o numero {cont[numero]}')
    resposta = ' '
    while resposta not in 'SN':
        resposta = str(input('Quer continua: ')).strip().upper()[0]
    if resposta == 'N':
        break