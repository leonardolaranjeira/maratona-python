
print('Exercício 83')

'''Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. Seu aplicativo deverá analisar 
se a expressão passada está com os parênteses abertos e fechados na ordem correta.'''

expre = str(input(f'Digite uma expressão: '))
expressoes = []

for parent in expre:
    if parent == '(':
        expressoes.append(parent)
    elif parent == ')':
        if not expressoes:
            print('Expressão inválida!')
            break
        expressoes.pop()
else:
    if not expressoes:
        print('Expressão válida!')
    else:
        print('Expressão inválida!')

    # Desafio concluído com ajuda!
