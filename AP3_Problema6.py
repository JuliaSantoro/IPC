def media(nota1, nota2, nota3, letra):
    if letra == "A":
        media_aritmetica = (nota1 + nota2 + nota3) / 3
        return media_aritmetica
    elif letra == "P":
        media_ponderada = (nota1 * 5 + nota2 * 3 + nota3 * 2) / (5 + 3 + 2)
        return media_ponderada
    else:
        return None  
