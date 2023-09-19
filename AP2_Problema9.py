
valor_produto = float(input("Digite o valor do produto: "))

estado = input("Digite a sigla do estado destino (MG, SP, PI, MS): ")

if estado == "MG":
    taxa_imposto = 0.07
elif estado == "SP":
    taxa_imposto = 0.12
elif estado == "PI":
    taxa_imposto = 0.15
elif estado == "MS":
    taxa_imposto = 0.08
else:
    print("Estado inválido")
    taxa_imposto = 0

if taxa_imposto > 0:
    preco_final = valor_produto * (1 + taxa_imposto)
    print(f"Valor final: {preco_final:.2f}")
