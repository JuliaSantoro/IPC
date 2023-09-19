def estacionamento(hora_entrada, minuto_entrada, hora_saida, minuto_saida):
    # Verifica se o estacionamento funciona entre 08:00 e 18:00
    if hora_entrada < 8 or hora_entrada >= 18 or hora_saida < 8 or hora_saida >= 18:
        return "Horário de funcionamento do estacionamento é entre 08:00 e 18:00"
    
    # Calcula o tempo de estacionamento em minutos
    tempo_estacionado = (hora_saida * 60 + minuto_saida) - (hora_entrada * 60 + minuto_entrada)
    
    # Calcula o número de horas a pagar arredondando para cima
    horas_a_pagar = (tempo_estacionado + 59) // 60
    
    # Calcula o valor total devido (R$1 por hora)
    valor_total = horas_a_pagar
    
    return f"Preço: R$ {valor_total:.2f}"

# Exemplos de uso da função
print(estacionamento(8, 0, 8, 1))
print(estacionamento(12, 30, 15, 31))
