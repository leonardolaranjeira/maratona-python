from time import sleep

Fvermelho_pretoB = '\033[1:30:41m'
verdeB = '\033[1:32m'
roxoB = '\033[1:35m'
amareloB = '\033[1:33m'
vermelhoB = '\033[1:31m'
limpa = '\033[m'

print('{}Exercício 43{}'.format(verdeB, limpa))

'''Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu status, de acordo 
com a tabela abaixo:

    - Abaixo de 18.5: Abaixo do peso
    - Entre 18.5 e 25: Peso ideal
    - 25 até 30: Sobrepeso
    - 30 até 40: Obesidade
    - Acima de 40: Obesidade mórbida'''

print('Calcule o IMC desejado!')

peso = float(input('Digite o seu peso: '))
altura = float(input('Digite a sua altura: '))

print('Verificando...')
sleep(2)
imc = peso / altura**2

if imc < 18.5:
    print('Você está {}ABAIXO DO PESO!{}'.format(amareloB, limpa))
elif imc == 18.5 or imc < 25:
    print('Você está no {}PESO IDEAL!{}'.format(verdeB, limpa))
elif imc == 25 or imc < 30:
    print('Você está com {}SOBRE PESO!{}'.format(roxoB, limpa))
elif imc == 30 or imc < 40:
    print('Você está com {}OBESIDADE!{}'.format(vermelhoB, limpa))
else:
    print('Você está com {}OBESIDADE MÓRBIDA!{}'.format(Fvermelho_pretoB, limpa))

# Desafio concluído!
