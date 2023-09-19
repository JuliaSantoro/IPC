lado1 = float(input("Digite o valor do primeiro lado: "))
lado2 = float(input("Digite o valor do segundo lado: "))
lado3 = float(input("Digite o valor do terceiro lado: "))


def verifica_triangulo(x, y, z):
    if x < y + z and y < x + z and z < x + y:
        return True
    else:
        return False

def tipo_triangulo(x, y, z):
    if x == y == z:
        return "Equilátero"
    elif x == y or y == z or x == z:
        return "Isósceles"
    else:
        return "Escaleno"

if verifica_triangulo(lado1, lado2, lado3):
    tipo = tipo_triangulo(lado1, lado2, lado3)
    print(tipo)
else:
    print("Não forma triângulo")
