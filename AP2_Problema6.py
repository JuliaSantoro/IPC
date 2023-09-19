
custo_carro = float(input("Digite o custo de fábrica do carro: "))

if custo_carro <= 12000.00:
    distribuidor = custo_carro * 0.05
elif custo_fabrica <= 25000.00:
    distribuidor = custo_carro * 0.10
else:
    distribuidor = custo_carro * 0.15


if custo_carro <= 12000.00:
    imposto = 0
elif custo_carro <= 25000.00:
    imposto = custo_carro * 0.15
else:
    impostos = custo_carro * 0.20

total = custo_carro +distribuidor + imposto


print(f"O custo total ao consumidor é: R$ {custo_total:.2f}")
