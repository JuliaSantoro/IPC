def pagamento(salario_atual):
    if salario_atual <= 280.00:
        aumento = 1.20
    elif salario_atual <= 700.00:
        aumento = 1.15
    elif salario_atual <= 1500.00:
        aumento = 1.10
    else:
        aumento = 1.05

    novo_salario = salario_atual * aumento
    return novo_salario

salario = float(input("Digite o valor do salário: "))
novo_salario = pagamento(salario)

print(f"Valor do aumento: {novo_salario - salario:.2f}")
print(f"Novo salário: {novo_salario:.2f}")
