
print('Exercício 35')

'''Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar 
um triângulo.'''

print('-=' * 20)
print('Analisador de triângulos!')
print('-=' * 20)

a = float(input('Digite o primeiro segmento: '))
b = float(input('Digite o segundo segmento: '))
c = float(input('Digite o terceiro segmento: '))

if a < b + c and b < a + c and c < a + b:
    print('Os segmentos acima PODEM FORMAR um triângulo!')
else:
    print('Os segmentos acima NÃO PODEM FORMAR um triângulo!')

# Desafio concluído!
