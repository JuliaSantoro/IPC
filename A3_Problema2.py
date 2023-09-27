def consumo(distancia, litros):
    consumo_medio = distancia / litros
    
    if consumo_medio < 8:
        return "Venda o carro!"
    elif 8 <= consumo_medio <= 12:
        return "Econômico!"
    else:
        return "Super econômico!"
