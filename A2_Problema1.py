
pontuacao_total = 0

for i in range(3):
    distancia_arremesso = float(input(f"Digite o {i + 1}º arremesso (-1 para lance livre): "))
    if distancia_arremesso == -1:
        pontuacao_total += 1
    elif distancia_arremesso > 7.24:
        pontuacao_total += 3
    elif distancia_arremesso <= 7.24:
        pontuacao_total += 2

print(f"Pontuação: {pontuacao_total}")
