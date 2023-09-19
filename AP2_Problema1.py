n1 = int(input("Digite o primeiro inteiro: "))
n2 = int(input("Digite o segundo inteiro: "))
n3 = int(input("Digite o terceito inteiro: "))
n4 = int(input("Digite o quarto inteiro: "))
n5 = int(input("Digite o quinto inteiro: "))


# Inicialize as variáveis para rastrear o maior, o menor e a contagem de divisíveis por 3
maior = menor = None
divisiveis_por_3 = 0

# Loop para ler cinco números inteiros
for i in range(5):
    numero = int(input(f"Digite o {i + 1}º inteiro: "))
    
    # Atualiza o maior e o menor, conforme necessário
    if maior is None or numero > maior:
        maior = numero
    if menor is None or numero < menor:
        menor = numero
    
    # Verifica se o número é divisível por 3
    if numero % 3 == 0:
        divisiveis_por_3 += 1

# Exibe os resultados
print(f"Maior: {maior}")
print(f"Menor: {menor}")
print(f"Quantidade de divisíveis por 3: {divisiveis_por_3}")
