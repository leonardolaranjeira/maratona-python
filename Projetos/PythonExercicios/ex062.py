from time import sleep
print('Exercício 62')

'''Melhore o DESAIO 061, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerra quando 
ele disser que quer mostrar zero termos.'''

print('-=' * 20)
print(f'{' ' * 10}PROGRESSÃO ARITMÉTICA{' ' * 10}')
print('-=' * 20)

pri_termo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))

primeiro = pri_termo - razao
enesimo = pri_termo + (10 - 1) * razao

while primeiro != enesimo:
    primeiro += razao
    print(f'{primeiro} > ', end='')
    if primeiro == enesimo:
        print('PAUSA')

while True:
    qtd_termos = int(input('Quantos termos você quer mostrar a mais? '))
    if qtd_termos == 0:
        print('Encerrando...')
        sleep(2)
        break
    else:
        for n in range(1, qtd_termos + 1):
            primeiro += razao
            print(f'{primeiro} > ', end='')
        print('PAUSA')

        # Desafio parcialmente concluído!
