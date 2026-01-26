#  Maior e Menor valores na Lista.

maior = menor = cont = 0
valores = list()
for c in range(0, 3):
    valores.append(int(input(f'Digite um valor na Posição {c}: ')))

    if c == 0:
        maior = menor = valores[c]
    else:
        if valores[c] > maior:
            maior = valores[c]
        if valores[c] < menor:
            menor = valores[c]

print(f'Voce digitou os valores {valores}')
for i, v in enumerate(valores):
    if v == maior:
        print(f'O maior valor digita foi {maior} e apareceu nas posiçoes {i}')

for i, v in enumerate(valores):
    if v == menor:
        print(f'O menor valor digitado foi {menor} e apareceu na posições {i}')