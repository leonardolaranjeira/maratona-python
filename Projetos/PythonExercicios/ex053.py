
print('-=' * 20)
print('Exercício 53')
print('-=' * 20)

'''Crie um programa que leia uma frase qualquer e diga se ela é um PALÍNDROMO, desconsiderando os espaços
    - APOS A SOPA
    - A SACADA DA CASA
    - A TORRE DA DERROTA
    - O LOBO AMA O BOLO
    - ANOTARAM A DATA DA MARATONA'''

print('Sua frase é um PALÍNDROMO?')

frase = str(input('Digite sua frase: ')).replace(' ', '').upper()
esarf = frase[::-1]

print(f'Sua frase sem espaços: {'\033[1:32m'}{frase}{'\033[m'}')
print(f'Sua frase invertida e sem espaços: {'\033[1:33m'}{esarf}{'\033[m'}')

if frase == esarf:
    print('Está frase É um PALÍNDROMO.')
else:
    print('Está frase NÃO É um PALÍNDROMO.')

# Desafio concluído
