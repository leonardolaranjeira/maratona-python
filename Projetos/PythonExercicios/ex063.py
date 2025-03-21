
print('Exercício 63')

'''Escreva um programa que leia um número "n" inteiro qualquer e mostre na tela os "n" primeiros elementos de uma 
sequência de Fibonacci.
Ex: 0 > 1 > 1 > 2 > 3 > 5 > 8...'''

print('Sequência de Fibonacci')

qtde_termos = int(input('Quantos termos você quer mostrar? '))
# 1. O usuário escolhe a quantidade de termos na sequência!

n1 = 0
n2 = 1  # 1. 0 e 1 são sempre os primeiros números da sequência de Fibonacci (É uma regra!).

print(f'{n1} > {n2}', end='')  # 2. Aqui estou pedindo para os 2 primeiros números sejam mostrados.
cont = 3  # 3. A contagem da sequencia se inicia no 3 pois a primeira e segunda são sempre as mesmas!
while cont <= qtde_termos:
    # 4. Enquanto a contagem for menor ou igual a quantidade de termos, o loop prossegue!
    n3 = n1 + n2  # 5. Na sequencia de Fibonacci a regra é sempre o último número + o penúltimo!
    print(f' > {n3}', end='')  # 6. Aqui estou pedindo para o terceiro número da sequência.
    n1 = n2
    n2 = n3  # 7. para a contagem prosseguir até o enésimo número, é apartir desta parte do loop o número anterior se
# torna o próximo até que chegue na quantidade de termos escolhidos!
    cont += 1  # 8. Ao chegar nesta etapa do loop, se conta mais um termo e prossegue até atingir a condição "While".
print(' > FIM')

# Desafio corrigído (Não consegui achar uma maneira prática de resolver!)
