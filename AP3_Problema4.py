litros = float(input("Digite a quantidade de litros: "))
tipo = input("Digite o tipo de combustível (a para Álcool ou g para Gasolina): ")
preco_litro = float(input("Digite o preço do litro de combustível: "))

def calcula_valor (preco_litro, litros_abastecidos, tipo_combustivel):
    if tipo_combustivel == "a":
        if litros_abastecidos <= 20:
            desconto_por_litro = 0.03
        else:
            desconto_por_litro = 0.05
    elif tipo_combustivel == "g":
        if litros_abastecidos <= 20:
            desconto_por_litro = 0.04
        else:
            desconto_por_litro = 0.06
    else:
        raise ValueError("Tipo de combustível inválido. Use 'a' para Álcool ou 'g' para Gasolina.")

    total = preco_litro * litros_abastecidos * (1 - desconto_por_litro)
    return total


total = calcula_valor(preco_litro, litros, tipo)
print(f"Total: {total:.2f}")
