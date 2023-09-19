hora = float(input("Digite o valor da hora trabalhada: "))
horas_traba = float(input("Digite a quantidade de horas trabalhadas: "))

def pagamento(hora, horas_trab):
    salario_bruto = hora * horas_traba

    if salario_bruto <= 900.00:
        desconto = 0
    elif salario_bruto <= 1500.00:
        desconto = salario_bruto * 0.05
    elif salario_bruto <= 2500.00:
        desconto = salario_bruto * 0.10
    else:
        desconto = salario_bruto * 0.20

    salario_liquido = salario_bruto - desconto
    return salario_bruto, desconto, salario_liquido

print(f"Salário bruto: {salario_bruto:.2f}")
print(f"Desconto: {desconto_ir:.2f}")
print(f"Salário líquido: {salario_liquido:.2f}")
