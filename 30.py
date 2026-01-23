# Funções para votação
def voto(ano):
    from datetime import datetime
    atual = datetime.now().year
    idade = atual - ano
    if idade < 16:
        return f'Com {idade} anos: NÃO VOTA'
    elif 16 <= idade < 18 or idade > 65:
        return f'Com {idade} anos: Voto OPCIONAL'
    else:
        return f'Com {idade} anos: Voto OBRIGATORIO'
    
nasc = int(input('Em que ano você nasceu: '))
print(voto(nasc))