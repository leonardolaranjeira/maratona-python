from time import sleep
print('Exercício 67')

'''Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. 
O programa será interrompido quando o número solicitado for negativo.'''

cont = 0
while True:
    tab = int(input('Digite qual tabuada gostaria de ver: '))
    print('=-' * 20)
    if tab == 0:
        print('Número núlo não tem tabuada!')
    elif tab < 0:
        print('Encerrando programa...')
        sleep(2)
        break
    cont += 1
    if tab >= 1:
        print(f'Tabuada do {tab}.')
        print('=-' * 20)
        for c in range(0, 11):
            mult = tab * c
            print(f'{tab} x {c:2} = {mult:2}')
        print('=-' * 20)

# Desafio concluído!
