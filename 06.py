# Contando vogais em Tupla

lista = ('caderno', 'legal', 'felicidade', 'ano', 'alegria')

for p in lista:
    print(f'\nNa palavras {p.upper()} temos ', end='')
    for letras in p:
        if letras.lower() in 'aeiou':
            print(letras, end=' ')