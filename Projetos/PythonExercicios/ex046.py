from time import sleep
print('Exercício 46')

'''Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifício, indo de 10 até 0,
com uma pausa de 1 segundo entre eles.'''

print('CONTAGEM REGRESSIVA PARA OS FOGOS DE ARTIFÍCIOS!')

for c in range(10, 0 - 1, -1):
    sleep(1)
    print(c)
sleep(1)
print('La vem os fogos!!!\n🎆🎇✨🎉🎊')

# Desafio concluído!
