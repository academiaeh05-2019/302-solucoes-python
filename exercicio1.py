# Empréstimo

idade = int(input("Digite sua idade: "))
renda = float(input("Digite sua renda: "))
valor = float(input("Digite o valor do empréstimo: "))

if idade < 21 or idade > 55:
    print("Idade não condiz com as regras do contrato")
elif renda < 1000:
    print("Renda insuficiente")
elif valor <= 0 or valor > renda * 15:
    print("Valor fora dos parâmetros definidos")
else:
    print("Emprestimo aprovado")
    parcelas = int(input("Em quantas parcelas você deseja pagar: "))
    if parcelas < 3 or parcelas > 9000:
      print("Numero de parcelas deve ser entre 3 e 12")
    else:
      total = valor +  parcelas * 0.045 * valor
      valor_parcela = total / parcelas
      print(f"O valor total de pagamento é R${round(total, 2)} dividido em {parcelas} parcelas de R${round(valor_parcela, 2)}")
