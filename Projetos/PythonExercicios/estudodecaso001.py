
AMARELO = '\033[1:33m'
VERDE = '\033[1:32m'
VERMELHO = '\033[1:31m'
AZUL = '\033[1:34m'
LIMPA = '\033[m'
BOLD = '\033[1:38m'

""" Desenvolva um programa de calculadora simples que possa realizar as seguintes operações: adição, subtração,
multiplicação e divisão. O programa deve solicitar ao usuário que digite dois números e a operação desejada,
e então exibir o resultado."""

print(f'{BOLD}{'ESTUDO DE CASO!':^60}{LIMPA}')
print('-=' * 30)
print(f'{AMARELO}{'CALCULADORA SIMPLES':^60}{LIMPA}')
print('-=' * 30)

numeros = []
operador = ''
resultado = []

for i, c in enumerate(range(2)):
    num = int(input(f'Digite o {c + 1}° número: '))
    numeros.append(num)
    if i == 1:
        print('-=' * 30)
        operador = str(input(f'Digite um dos operadores que deseja usar:\n'
                             f'{VERMELHO}ADIÇÃO: +{LIMPA}\n'
                             f'{AZUL}SUBTRAÇÃO: -{LIMPA}\n'
                             f'{AMARELO}DIVISÃO: /{LIMPA}\n'
                             f'{VERDE}MULTIPLICAÇÃO: *{LIMPA}\n'
                             '>>> Qual operador deseja executar [+, -, * ou /]: '))

        if operador == '+':
            resultado = numeros[0] + numeros[1]
            break
        elif operador == '-':
            resultado = numeros[0] - numeros[1]
            break
        elif operador == '*':
            resultado = numeros[0] * numeros[1]
            break
        elif operador == '/':
            resultado = numeros[0] / numeros[1]
            break
        else:
            print(f'{VERMELHO}OPERAÇÃO INVÁLIDA!{LIMPA}')
            break

if operador in '+-*/':
    print('-=' * 30)
    print(f'Os valores digitados foram: {numeros[0]} {operador} {numeros[1]}')
    print(f'O resultado desta operação fica: {VERDE}{resultado:.2f}{LIMPA}')
    print('-=' * 30)


