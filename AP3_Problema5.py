
altura = float(input("Digite a altura: "))
sexo = str(input("Digite o sexo (F/M): "))

def peso_ideal(altura, sexo):
    if sexo == "F":
        peso_ideal = (62.1 * altura) - 44.7
    elif sexo == "M":
        peso_ideal = (72.7 * altura) - 58
    else:
        peso_ideal = None  # Sexo não reconhecido
    return peso_ideal
