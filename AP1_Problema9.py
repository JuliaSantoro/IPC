reais = input("Digite o valor em reais: ")
reais = float(reais)

cotacao = input("Digite a cotação do dólar: ")
cotacao = float(cotacao)

dolar = reais/cotacao

print("Valor em dólar: %.2f" % (dolar))


