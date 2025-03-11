
print('Exercício 102')

'''Crie um programa que tenha uma função fatorial() que receba dois parâmetros: o primeiro que indique o número a 
calcular e o outro chamado show, que será um valor lógico(opcional) indicando se será mostrado ou não na tela o 
processo de cálculo do fatorial.'''

def fatorial(num, show):
    mult = 1
    if show == 1:
        print(f'{num}! = ', end='')
        for v in range(num, 0, -1):
            if v > 1:
                print(f'{v} ', end='x ')
            else:
                print(f'{v} ', end='= ')
            mult *= v
        return mult
    else:
        for v in range(num, 0, -1):
            mult *= v
        return mult


while True:
    print('-=' * 30)
    n = int(input('Digite um valor: '))
    decisao = int(input('Quer mostrar o processo fatorial (0 > Não / 1 > Sim)? '))

    if decisao in [0, 1]:
        resp = fatorial(n, decisao)
        print(resp)
        break
    else:
        print('Opção inválida, tente novamente!')

# Desafio Concluído!
