def calcula_valor(preco_litro, litros, tipo_combustivel):
    if tipo_combustivel == "a":
        if litros <= 20:
            desconto = 0.03
        else:
            desconto = 0.05
    elif tipo_combustivel == "g":
        if litros <= 20:
            desconto = 0.04
        else:
            desconto = 0.06
    else:
        raise ValueError("Tipo de combustível inválido. Use 'a' para álcool ou 'g' para gasolina.")

    valor_pago = preco_litro * litros * (1 - desconto)
    return valor_pago
