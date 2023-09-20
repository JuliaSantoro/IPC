salario = float(input("Digite o valor do salário: "))

def mudanca(salario_atual):
    if salario_atual <= 280.00:
        aumento = salario_atual * 0.20
    elif salario_atual <= 700.00:
        aumento = salario_atual * 0.15
    elif salario_atual <= 1500.00:
        aumento = salario_atual * 0.10
    else:
        aumento = salario_atual * 0.05

    novo_salario = salario_atual + aumento
    return novo_salario

novo_salario = mudanca(salario)

print(f"Valor do aumento: {novo_salario - salario:.2f}")
print(f"Novo salário: {novo_salario:.2f}")
