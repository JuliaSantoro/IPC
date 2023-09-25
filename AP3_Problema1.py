def pagamento(salario_atual):
    if salario_atual <= 280.00:
        aumento = 0.20
    elif salario_atual <= 700.00:
        aumento = 0.15
    elif salario_atual <= 1500.00:
        aumento = 0.10
    else:
        aumento = 0.05

    novo_salario = (salario_atual * aumento) + salario_atual
    return novo_salario



