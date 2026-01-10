# Boletim com listas compostas
notas = []

while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    notas.append([nome, [nota1, nota2], media])
    

    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar: ')).strip().upper()
    if resp == 'N':
        break
print(f'{"No.":<4}{"NOME":<10}{"MÉDIA":>8}')
for i, a in enumerate(notas):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
while True:
    opc = int(input('Mostrar a nota de qual aluno: [999 para STOP]'))
    if opc == 999:
        print('Programa finalizado...')
        break
    if opc <= len(notas) -1:
        print(f'Notas de {notas[opc][0]} são {notas[opc][1]}')