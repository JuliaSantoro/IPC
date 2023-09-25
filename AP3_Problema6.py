def media(nota1, nota2, nota3, tipo_media):
    if tipo_media == "A":
        media_aritmetica = (nota1 + nota2 + nota3) / 3
        return media_aritmetica
    elif tipo_media == "P":
        media_ponderada = (nota1 * 5 + nota2 * 3 + nota3 * 2) / 10
        return media_ponderada
    else:
        raise ValueError("Tipo de média inválido. Use 'A' para média aritmética ou 'P' para média ponderada.")
