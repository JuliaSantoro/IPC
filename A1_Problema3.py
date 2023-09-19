
numero = int(input("Digite um inteiro de 4 algarismos: "))
milhar = numero // 1000
centena = (numero % 1000) // 100
dezena = (numero % 100) // 10
unidade = numero % 10
soma = milhar + centena + dezena + unidade
print(f"Resultado: {soma}")
