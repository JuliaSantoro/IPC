def verifica_triangulo(lado1, lado2, lado3):
    # Verifica a desigualdade triangular
    if lado1 < lado2 + lado3 and lado2 < lado1 + lado3 and lado3 < lado1 + lado2:
        return True
    else:
        return False

def tipo_triangulo(lado1, lado2, lado3):
    if lado1 == lado2 and lado2 == lado3:
        return "Equilátero"
    elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
        return "Isósceles"
    else:
        return "Escaleno"
