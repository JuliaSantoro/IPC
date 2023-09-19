altura = float(input("Digite a aultura: "))
sexo = str(input("Digite o sexo (F/M): "))

peso_ideal = if(sexo = "F"):
                (62.1 * altura) - 44.7  
             elif(sexo = "M"):
                (72.7 * altura) - 58
print(f"Peso ideal: {peso_ideal}")
 
