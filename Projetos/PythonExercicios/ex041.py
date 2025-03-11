
vermelhoB = '\033[1:31m'
Fpreto_cinza = '\033[7:30:47m'
verdeB = '\033[1:32m'
azulB = '\033[1:34m'
roxoB = '\033[1:35m'
Fazul_brancaB = '\033[1:30:46m'
limpa = '\033[m'

print('{}Exercício 41{}'.format(verdeB, limpa))

'''A confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre 
sua categoria, de acordo com a idade:

    - Até 9 anos: MIRIM
    - Até 14 anos: INFANTIL
    - Até 19 anos: JUNIOR
    - Até 25 anos: SÊNIOR
    - Acima: MASTER'''

print('{}Confira agora qual o seu nível como nadador!'.format(Fazul_brancaB))

idade = int(input('{}Qual a sua idade? '.format(limpa)))

if idade <= 9:
    print('Você é um nadador {}MIRIM{}'.format(roxoB, limpa))
elif idade <= 14:
    print('Você é um nadador {}INFANTIL{}'.format(azulB, limpa))
elif idade <= 19:
    print('Você é um nadador {}JUNIOR{}'.format(verdeB, limpa))
elif idade <= 25:
    print('Você é um nadador {}SÊNIOR{}'.format(vermelhoB, limpa))
else:
    print('Você é um nadador {}MASTER{}'.format(Fpreto_cinza, limpa))

# Desafio concluído!
