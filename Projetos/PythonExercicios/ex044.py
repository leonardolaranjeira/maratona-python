print('Exercício 44')

'''Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e 
condição de pagamento:
    - À vista (dinheiro/pix): 10% de desconto
    - À vista no débito: 5% de desconto
    - Em até 2x no cartão: preço normal
    - 3x ou mais no cartão: 20% de juros'''

print('Sistema de acerto de contas!')

valor = float(input('Digite o valor da compra: '))
pgto = int(input('Qual a forma de pagamento?\n'
                 '1) Pix / Dinheiro\n'
                 '2) Débito\n'
                 '3) Crédito 2x\n'
                 '4) Crédito 3x\n'
                 'Digite aqui: '))
pgto1 = int(str(pgto)[0])

vista = valor * 0.1
debito = valor * 0.05
credito2x = valor / 2
credito3x = (valor * 0.2) + valor

if pgto1 == 1:
    print('O valor da compra fecha no valor de R${:.2f} com 10% de desconto no pix/dinheiro!'.format(valor - vista))
elif pgto1 == 2:
    print('O valor da compra fecha no valor de R${:.2f} com 5% de desconto no débito!'.format(valor - debito))
elif pgto1 == 3:
    print('O valor da compra fecha no valor de R${:.2f} sem juros.'
          '\nFicando em 2 parcelas de R${:.2f}.'.format(credito2x, credito2x / 2))
elif pgto1 == 4:
    vzs = int(input('Quantas vezes? '))
    credito3x = (valor * 0.2) + valor
    print('O valor da compra fecha no valor de R${:.2f} com 20% de juros.'
          '\nFicando em {} parcelas de R${:.2f}.'.format(credito3x, vzs, credito3x / vzs))
else:
    print('Está não é uma das formas de pagamento disponíveis!')

# Desafio concluído!
