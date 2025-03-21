
print('Exercício 75')

'''Desenvolva um programa que leia 4 valores pelo teclado e guarde-os em um tupla. No final, mostre:
    A) Quantas vezes apareceu o valor 9.
    B) Em que posição foi digitado o primeiro valor 3.
    C) Quais foram os números pares.'''

tupla = (int(input('Digite um valor: ')), int(input('Digite um valor: ')), int(input('Digite um valor: ')),
         int(input('Digite um valor: ')))

pares = []

print(f'O valor 9 apareceu: {tupla.count(9)} vez(es).')

encontrado = False
for num in tupla:
    if num == 3 and not encontrado:
        print(f'O primeiro número 3 foi digitado na {tupla.index(3) + 1}° posição.')
        encontrado = True
    # Este bloco busca a primeira escolha do número 3 e faz com que as outras vezes que o
    # usuário digita algum valor sejam ignoradas.

for par in tupla:
    if par % 2 == 0:
        pares.append(par)

print(f'Os números pares da tupla são: ', end='')
for index, num in enumerate(pares):
    if index == len(pares) - 1:
        print(f'{num}.')
    elif index < len(pares) - 1:
        print(f'{num}, ', end='')
        # Este bloco for faz com que separe os valores digitados com "," e o ultimo número seja "."

# Desafio concluído!
