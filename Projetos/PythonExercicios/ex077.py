
print('Resolução do exercício 77')

'''Crie um programa que tenha uma tupla com várias palavras (não usar acentos). Depois disso, você deve mostrar para 
cada palavra, quais são as suas vogais.'''

palavras = ('AMERICANO', 'NORTE', 'AMOR', 'PICOLE', 'MUSICA', )

for palavra in palavras:
    print(f'\nNa palavra {palavra} temos: ', end='')
    for letra in palavra:
        if letra.upper() in 'AEIOU':
            print(letra, end=' ')

# Desafio corrigido!
