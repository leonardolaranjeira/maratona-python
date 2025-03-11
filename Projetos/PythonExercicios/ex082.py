
print('Exercício 82')

'''Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas extras que 
vão conter apenas os valores pares e os valores impares digitados respectivamente. Ao final, mostre o conteúdo
das três listas geradas.'''

pares = []
impares = []
numeros = []
cont = 0

while True:
    cont += 1
    num = int(input(f'Digite o {cont}° número (Digite "999" para parar): '))
    numeros.append(num)

    if num == 999:
        numeros.pop()
        break
    if num % 2 == 0:
        pares.append(num)
    else:
        impares.append(num)

print('-=' * 30)
print(f'Os números digitados foram: {numeros}')
print(f'Os números pares digitados foram: {pares}')
print(f'Os números ímpares digitados foram: {impares}')
print('-=' * 30)

# Desafio concluído!
