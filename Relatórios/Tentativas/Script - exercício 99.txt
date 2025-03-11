
print('Exercício 99')

'''Faça um programa que tenha uma função chamada maior(), que recebe vários parâmetros com valores inteiros. Seu
programa tem que analisar todos os valores e dizer qual deles é o maior.'''

valor = 0


def maior():
    valores = []
    while True:
        valor = int(input('Digite um valor (999 para parar): '))

        if valor == 999:
            print('=-' * 34)
            print('Analisando os valores passados!')
            for n in valores:
                print(f'{n} ', end='')
            print(f'Foram informados {len(valores)} valores ao todo.')
            print(f'O maior valor informado foi: {max(valores)}')
            print('=-' * 34)
            print('<< ENCERRANDO >>')
            break

        valores.append(valor)


maior()

# Desafio concluído!
