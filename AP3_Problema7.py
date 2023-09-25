def operacao(valor1, valor2, simbolo):
    if simbolo == "+":
        resultado = valor1 + valor2
    elif simbolo == "-":
        resultado = valor1 - valor2
    elif simbolo == "*":
        resultado = valor1 * valor2
    elif simbolo == "/":
        if valor2 == 0:
            raise ValueError("Não é possível dividir por zero.")
        resultado = valor1 / valor2
    else:
        raise ValueError("Símbolo de operação inválido. Use '+', '-', '*', ou '/'.")

    return resultado
