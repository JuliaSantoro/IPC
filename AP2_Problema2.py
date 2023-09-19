vel_maxima = float(input("Digite o valor da velocidade máxima: "))
vel_registrada = float(input("Digite o valor da velocidade registrada: "))
resultado = velocidade_registrada - velocidade_maxima

if resultado <= 0:
    print("Sem Infração")
elif resultado <= 0.2 * velocidade_maxima:
    print("Infração Média")
elif resultado <= 0.5 * velocidade_maxima:
    print("Infração Grave")
else:
    print("Infração Gravíssima") 
