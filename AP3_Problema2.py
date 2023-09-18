def pagamento(valor_hora, horas_trabalhadas):
    salario_bruto = valor_hora * horas_trabalhadas

    if salario_bruto <= 900.00:
        desconto_ir = 0
    elif salario_bruto <= 1500.00:
        desconto_ir = salario_bruto * 0.05
    elif salario_bruto <= 2500.00:
        desconto_ir = salario_bruto * 0.10
    else:
        desconto_ir = salario_bruto * 0.20

    salario_liquido = salario_bruto - desconto_ir
    return salario_bruto, desconto_ir, salario_liquido

# Exemplos de uso da função
valor_hora = float(input("Digite o valor da hora trabalhada: "))
horas_trabalhadas = float(input("Digite a quantidade de horas trabalhadas: "))

salario_bruto, desconto_ir, salario_liquido = pagamento(valor_hora, horas_trabalhadas)

print(f"Salário bruto: {salario_bruto:.2f}")
print(f"Desconto: {desconto_ir:.2f}")
print(f"Salário líquido: {salario_liquido:.2f}")
