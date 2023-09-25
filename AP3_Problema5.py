def peso_ideal(altura, sexo):
    if sexo == "F":
        peso = (62.1 * altura) - 44.7
    elif sexo == "M":
        peso = (72.7 * altura) - 58
    else:
        raise ValueError("Sexo inválido. Use 'F' para feminino ou 'M' para masculino.")
    
    return peso
