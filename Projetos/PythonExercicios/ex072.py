
print('Exercício 72')

'''Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de zero até vinte. Seu 
programa deverá ler um número pelo teclado (entre 0 a 20) e mostrá-lo por extenso.'''

contagem = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze',
            'Treze', 'Quatorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')

while True:
    valor = int(input('Digite um valor de 0 a 20: '))
    print('=-' * 30)
    while valor < 0 or valor > 20:
        print('Valor inválido, Tente novamente.')
        valor = int(input('Digite um valor de 0 a 20: '))
        print('=-' * 30)

    if 0 <= valor <= 20:
        print(f'O valor escolhido foi {valor} e seu nome por extenso é: {contagem[valor]}.')
        print('=-' * 30)

    decisao = str(input('Deseja escolher outro número? [S/N]\n')).strip().upper()[0]
    while decisao != 'N' and decisao != 'S':
        print('Opção inválida. Tente novamente!')
        print('=-' * 30)
        decisao = str(input('Deseja escolher outro número? [S/N]\n')).strip().upper()[0]
        print('=-' * 30)

    if decisao == 'N':
        print('Encerrando programa...')
        break

# Desafio concluído!
