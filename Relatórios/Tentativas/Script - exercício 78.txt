
print('Exercício 78')

'''Faça um programa que leia 5 valores númericos e guarde-os em uma lista. No final, mostre qual foi o maior e o 
menor valor digitado e as suas respectivas posições na lista.'''


valores = []
indice_ma = []
indice_me = []
maior = []
menor = []

for p in range(0, 5):
    valor = int(input(f'Digite um valor para na posição {p}: '))
    valores.append(valor)

    maior = valores[0]
    menor = valores[0]
    indice_ma = []
    indice_me = []

    for i, valor in enumerate(valores):
        if valor > maior:
            maior = valor
            indice_ma = [i]
        elif valor == maior:
            indice_ma.append(i)

        if valor < menor:
            menor = valor
            indice_me = [i]
        elif valor == menor:
            indice_me.append(i)

print('-=' * 30)
print(f'Você digitou os valores: {valores}')
print(f'O maior valor digitado foi {maior} na(as) posição(ões): {indice_ma}')
print(f'O menor valor digitado foi {menor} na(as) posição(ões): {indice_me}')

# Desafio concluído!
