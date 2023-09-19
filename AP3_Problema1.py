salario = float(input("Digite o valor do salário: "))

def novo_salario (salario):
    if salario <= 280.00:
        aumento = salario * 0.20
    elif salario <= 700.00:
        aumento = salario * 0.15
    elif salario <= 1500.00:
        aumento = salario * 0.10
    else:
        aumento = salario * 0.05

    novo_salario = salario + aumento
    return novo_salario

print(f"Valor do aumento: {novo_salario - salario:.2f}")
print(f"Novo salário: {novo_salario:.2f}")
