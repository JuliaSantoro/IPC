x = float(input("Digite o valor do primeiro lado: "))
y = float(input("Digite o valor do segundo lado: "))
z = float(input("Digite o valor do terceiro lado: "))


def eh_triangulo(x, y, z):
    if x < y + z and y < x + z and z < x + y:
        return True
    else:
        return False

    if eh_triangulo == true and x == y == z:
        print("Equilátero")
    elif eh_triangulo == true and (x == y or y == z or x == z):
        print("Isósceles")
    elif eh_triangulo == true and (x != y != z) 
   print("Escaleno")

else:
    print("Não forma triângulo")
