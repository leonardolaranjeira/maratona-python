from time import sleep

vermelhoB = '\033[1:31m'
verdeB = '\033[1:32m'
limpa = '\033[m'

print('Exercício 59')

'''Crie um programa que leia dois valores e mostre um menu como o que está abaixo:
    
    [1] SOMAR
    [2] MULTIPLICAR
    [3] MAIOR
    [4] NOVOS NÚMEROS
    [5] SAIR DO PROGRAMA
    
Seu programa deverá realizar a operação solicitada em cada caso.'''

print(f'{verdeB}Escolha dois valores!{limpa}')

valor1 = int(input('Primeiro valor: '))
valor2 = int(input('Segundo valor: '))

opcao = 0
while True:
    opcao = int(input('Escolha uma opção para prosseguir!\n'
                      '[1] SOMAR\n'
                      '[2] MULTIPLICAR\n'
                      '[3] MAIOR\n'
                      '[4] NOVOS NÚMEROS\n'
                      '[5] SAIR DO PROGRAMA\n'
                      '>>> Qual a sua opção? '))
    if opcao == 1:
        print(f'{vermelhoB}{valor1} + {valor2} SOMADOS fica... {valor1 + valor2}{limpa}')
    elif opcao == 2:
        print(f'{vermelhoB}{valor1} x {valor2} MULTIPLICADOS fica... {valor1 * valor2}{limpa}!')
    elif opcao == 3:
        if valor1 > valor2:
            print(f'{vermelhoB}Entre {valor1} e {valor2} o maior valor é: {valor1}{limpa}')
        elif valor2 > valor1:
            print(f'{vermelhoB}Entre {valor1} e {valor2} o maior valor é: {valor2}{limpa}')
    elif opcao == 4:
        print(f'{verdeB}Ok, escolha novamente os novos valores!{limpa}')
        valor1 = int(input('Primeiro valor: '))
        valor2 = int(input('Segundo valor: '))
    elif opcao == 5:
        print(f'{vermelhoB}Encerrando...{limpa}')
        sleep(2)
        break
    else:
        print(f'{vermelhoB}Está não é uma opção válida. Tente novamente!{limpa}')

# Desafio concluído!
