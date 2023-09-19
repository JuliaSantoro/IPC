def operacao(valor1, valor2, simbolo):
    if simbolo == "+":
        resultado = valor1 + valor2
    elif simbolo == "-":
        resultado = valor1 - valor2
    elif simbolo == "*":
        resultado = valor1 * valor2
    elif simbolo == "/":
        if valor2 != 0:  # Verifica se o divisor não é zero
            resultado = valor1 / valor2
        else:
            return "Erro: divisão por zero"
    else:
        return "Operação não reconhecida"
    
    return resultado
