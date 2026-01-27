# Validando entrada de dados em Python
def leiaInt(mensagem):
    while True:
        valor = input(mensagem)
        if valor.isdigit():
            return int(valor)
        else:
            print("Digite um número válido!")

n = leiaInt("Digite um numero: ")
print(f"Você acabou de digitar o número {n}")