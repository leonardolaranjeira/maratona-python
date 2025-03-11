
print('Exercício 80')

'''Crie um programa onde o usuário possa digitar cinco valores númericos e cadastre-os em uma lista, já na posição 
correta de inserção (sem usar o sort()); No final, mostre a lista ordenada na tela.'''

valores = []

for indice in range(5):
    valor = int(input(f'Digite o {indice + 1}° valor: '))

    if not valores:
        valores.append(valor)
        print(f'Adicionado a {indice + 1}° posição da lista...')
    else:
        inserido = False
        for i in range(len(valores)):
            if valor < valores[i]:
                valores.insert(i, valor)
                print(f'Adicionado a {i + 1}° posição da lista...')
                inserido = True
                break
        if not inserido:
            valores.append(valor)
            print(f'Adcionado o valor ao final da lista...')

print('=-' * 30)
print(f'Os valores digitados na ordem foram: {list(valores)}')
print('=-' * 30)

# Desafio concluído com ajuda!
