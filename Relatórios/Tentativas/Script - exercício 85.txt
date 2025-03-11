
print('Exercício 85')

'''Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única
que mantenha separados os valores pares e ímpares. No final mostre os valores pares e ímpares em ordem crescente.'''

valores = [[], []]

for i in range(0, 7):
    valor = int(input(f'Digite o {i + 1}° valor: '))
    if valor % 2 == 0:
        valores[0].append(valor)

    elif valor % 2 == 1:
        valores[1].append(valor)

print('=-' * 30)
print(f'Os valores PARES desta lista são: {sorted(valores[0])}')
print(f'Os valores ÍMPARES desta lista são: {sorted(valores[1])}')

# Desafio concluído!
