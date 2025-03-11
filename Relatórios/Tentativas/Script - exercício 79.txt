
print('Exercício 79')

'''Crie um programa onde o usuário possa digitar vários valores númericos e cadastre-os em uma lista. Caso o número 
já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, 
em ordem crescente'''

valores = set()
while True:
    valor = int(input('Digite um valor: (Digite "999" para parar)\n'))
    if valor == 999:
        print('-=' * 30)
        ordem = sorted(valores)
        print(f'Os valores digitados foram: {ordem}')
        break

    if valor in valores:
        print('Este valor já foi digitado, digite outro!')
    else:
        valores.add(valor)

# Desafio concluído!
