
dias_trabalhados = int(input("Digite a quantidade de dias trabalhados: "))

valor_diario = 30.00

valor_bruto = dias_trabalhados * valor_diario

imposto_renda = valor_bruto * 0.08

valor_liquido = valor_bruto - imposto_renda

print(f"Valor recebido: {valor_liquido:.2f}")
