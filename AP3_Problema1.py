def pagamento(salario_atual):
    if salario_atual <= 280:
        aumento = salario_atual * 0.20
    elif salario_atual <= 700:
        aumento = salario_atual * 0.15
    elif salario_atual <= 1500:
        aumento = salario_atual * 0.10
    else:
        aumento = salario_atual * 0.05

    novo_salario = salario_atual + aumento

    return novo_salario

