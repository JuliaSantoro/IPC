
distancia_arremesso = float(input("Digite a distância do arremesso à cesta (em metros): "))

pontuacao_total = 0

    if distancia_arremesso > 7.24:
        pontuacao_total += 3
    elif distancia_arremesso <= 7.24:
        pontuacao_total += 2
    else:
        pontuacao_total += 1

print(f"A pontuação total das três primeiras jogadas é: {pontuacao_total}")
