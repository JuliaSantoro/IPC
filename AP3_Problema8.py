def estacionamento(entrada_hora, entrada_minuto, saida_hora, saida_minuto):
    entrada_total_minutos = entrada_hora * 60 + entrada_minuto
    saida_total_minutos = saida_hora * 60 + saida_minuto

    if saida_total_minutos < 480 or entrada_total_minutos > 1080:
        return 0.00

    horas_estacionadas = (saida_total_minutos - entrada_total_minutos + 59) // 60

    preco = horas_estacionadas

    return preco
