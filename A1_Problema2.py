
pedro_investimento = float(input("Digite o valor que o Pedro apostou: "))

joao_investimento = float(input("Digite o valor que o João apostou: "))

marcela_investimento = float(input("Digite o valor que a Marcela apostou: "))


premio = float(input("Digite o valor do prêmio: "))

total_investido = pedro_investimento + joao_investimento + marcela_investimento


proporcao_pedro = pedro_investimento / total_investido

proporcao_joao = joao_investimento / total_investido

proporcao_marcela = marcela_investimento / total_investido


premio_pedro = proporcao_pedro * premio
premio_joao = proporcao_joao * premio
premio_marcela = proporcao_marcela * premio


print(f"Prêmio do Pedro: {premio_pedro:.2f}")
print(f"Prêmio do João: {premio_joao:.2f}")
print(f"Prêmio da Marcela: {premio_marcela:.2f}")
