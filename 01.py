numeros = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez')
numero = 0
numero = int(input('Digite um numero entre 0 e 10: '))
while numero > 10:
    numero = int(input('Tente novamente. Digite um numero entre 0 e 10: '))
    if numero == numeros:
        print(numeros)



print('end')