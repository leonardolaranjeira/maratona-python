
def leiadinheiro(msg):
    vermelho = '\033[1:31m'
    limpa = '\033[m'
    ok = False
    valor = 0.0
    while True:
        i = str(input(msg)).replace(',', '.')
        try:
            valor = float(i)
            ok = True
        except ValueError:
            print(f'{vermelho}Erro! Você digitou um valor inválido.{limpa}')

        if ok:
            break
    return valor
