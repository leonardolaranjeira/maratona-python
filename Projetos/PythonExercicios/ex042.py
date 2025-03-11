
Fcinza_pretoN = '\033[7:30:47m'
vermelhoB = '\033[1:31m'
verdeB = '\033[1:32m'
limpa = '\033[m'

print('{}Exercício 42{}'.format(verdeB, limpa))

'''Refaça o "DESAFIO 35" dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
    - EQUILÁTERO: Todos os lados são iguias
    - ISÓSCELES: Dois lados iguais
    - ESCALENO: Todos os lados diferentes'''

print('{}Escolha três valores e veja que tipo de triângulo as retas formam!{}'.format(Fcinza_pretoN, limpa))
l1 = int(input('Digite o primeiro valor: '))
l2 = int(input('Digite o segundo valor: '))
l3 = int(input('Digite o terceiro valor: '))

if l1 == l2 == l3:
    print('Estas retas formam um triângulo {}EQUILÁTERO{}'.format(vermelhoB, limpa))
elif l1 == l2 or l1 == l3 or l2 == l3:
    print('Estas retas formam um triângulo {}ISÓSCELES{}'.format(vermelhoB, limpa))
else:
    print('Estas retas formam um triângulo {}ESCALENO{}'.format(vermelhoB, limpa))

# Desafio concluído!
