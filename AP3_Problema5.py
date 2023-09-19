altura = float(input("Digite a altura: "))
sexo = input("Digite o sexo (F/M: ")

def peso_ideal(altura, sexo):
    if sexo == "F":
        peso_ideal = (62.1 * altura) - 44.7
    elif sexo == "M":
        peso_ideal = (72.7 * altura) - 58

    return peso_ideal

print("Peso ideal: %f " % (peso_ideal))
