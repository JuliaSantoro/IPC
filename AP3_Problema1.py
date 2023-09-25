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



