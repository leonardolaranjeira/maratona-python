
print('Exercício 36')

'''Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. O programa vai perguntar o 
"valor da casa", o "salário" do comprador e em "quantos anos" ele vai pagar. Calcule o valor da prestação mensal, 
sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado.'''

vlr_casa = float(input('Qual o valor do empréstimo que deseja fazer para a compra da casa? R$'))
salario = float(input('Qual o seu salário atual? R$'))
anos = int(input('Em quantos anos pretende pagar esta casa? '))
# Solicitação das informações necessárias ao usuário.

limite_prestacao = salario * 0.3  # Cálculo de 30% do salário do cliente!
meses = anos * 12  # total de meses para o pagamento!
prestacao = vlr_casa / meses  # Valor da mensalidade calculada!

if prestacao <= limite_prestacao:
    print('Empréstimo aprovado! \nO valor da casa em {} meses, ficará em uma média de R${:.2f} por mês!'
          .format(meses, prestacao))
else:
    print('Empréstimo negado! \nA prestação de R${:.2f} em {} meses, excede 30% do salário.'
          .format(prestacao, meses))

# Desafio concluído!
