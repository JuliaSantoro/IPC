def valor_energia(consumo_kWh, tipo_instalacao):
    if tipo_instalacao == 'R':
        if consumo_kWh <= 500:
            return consumo_kWh * 0.40
        else:
            return consumo_kWh * 0.65
    elif tipo_instalacao == 'C':
        if consumo_kWh <= 1000:
            return consumo_kWh * 0.55
        else:
            return consumo_kWh * 0.60
    elif tipo_instalacao == 'I':
        if consumo_kWh <= 5000:
            return consumo_kWh * 0.55
        else:
            return consumo_kWh * 0.60
    else:
        return "Tipo de instalação inválido."

