
print('Exercício 104')

'''Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante à função input() do Python,
só que fazendo a validação para aceitar apenas um valor numérico.
Ex: n = leiaInt('Digite um n')'''

vermelho = '\033[1:31m'
limpa = '\033[m'

def leiaint(string):
    if string.isdigit():
        num = int(string)
        print('-=' * 20)
        print(f'Você acabou de digitar o número {num}')
        return True
    else:
        print(f'{vermelho}Erro!\nDigite um inteiro válido!{limpa}')
        return False

desl = False

while not desl:
    print('-=' * 20)
    valor = str(input('Digite um número: ')).strip()
    desl = leiaint(valor)

# Desafio concluído! (Não totalmente correto)
