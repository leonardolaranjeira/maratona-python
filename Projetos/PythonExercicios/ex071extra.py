print('Exercício 71extra')

'''Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual será o valor
a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues.
OBS: Considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.'''

print('=' * 50)
print(f'{'BANCO TORANJO': ^50}')
print('=' * 50)

valor = int(input('Que valor você quer sacar? R$ '))

total = valor  # valor queo usuário precisa em notas de dinheiro!
cedula = 50  # A contagem inicia pelas notas de maior valor!
totcedulas = 0  # variável que será utilizada para contar e destribuir as notas de maneira correta para cada valor.
while True:
    if total >= cedula:
        total -= cedula
        totcedulas += 1  # Contagem das cédulas que vão ser entregues ao usuário!
    else:
        if totcedulas > 0:
            print(f'Total de {totcedulas} cédulas de R${cedula}')  # Impressão das quantidades destribuidas de notas.

        if cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 1
            '''Quando o valor total estiver igual ao valor de alguma das cédulas, o programa atualiza e faz
             a nova contagem do proximo valor de cédula'''

        totcedulas = 0  # após a contagem das cédulas, o total de cédulas reseta e faz a contagem do proximo valor.

        if total == 0:  # Quando o total do valor estiver zerado o programa para de contar as notas.
            break
print('=' * 50)
print('Volte sempre ao BANCO CEV! Tenha um bom dia!')

# Desafio corrigído!
