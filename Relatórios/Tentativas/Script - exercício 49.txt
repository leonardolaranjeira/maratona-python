
print(f'{'\033[1:32m'}Exercício 49')

'''Refaça o DESAFIO 009, mostrando a tabuáda de um número que o usuário escolher, 
só que agora utilizando um laço for.'''

print(f'{'\033[1:31m'}TABUADA')

num = int(input(f'{'\033[1m'}Escolha um número:{'\033[m'} '))

print(f'{'\033[1:32m'}TABUADA DO {'\033[1:33m'}{num}{'\033[1:32m'}!!!{'\033[1m'}')
for t in range(0, 11):
    print(f'{'\033[1:32m'}{num} x {t:2} = {'\033[1:33m'}{num * t:2}{'\033[m'}')
print(f'{'\033[1:31m'}FIM')

# Desafio concluído!
