def estacionamento(hora_chegada, minuto_chegada, hora_partida, minuto_partida):
    minutos_chegada = hora_chegada * 60 + minuto_chegada
    minutos_partida = hora_partida * 60 + minuto_partida

    tempo_total_minutos = float(minutos_partida - minutos_chegada)

    if tempo_total_minutos <= 120:
        return f"Preço: R$ {1:.2f}"
    elif 180 <= tempo_total_minutos <= 240:
        return f"Preço: R$ {1.4 * (tempo_total_minutos // 60):.2f}"
    else:
        return f"Preço: R$ {2 * (tempo_total_minutos // 60):.2f}"
