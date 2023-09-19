
dia = int(input("Digite o dia: "))
mes = int(input("Digite o mês: "))
ano = int(input("Digite o ano: "))

bissexto = (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0)

if mes < 1 or mes > 12:
    print("Data inválida")
else:
    if mes == 2: 
        if (bissexto and 1 <= dia <= 29) or (not bissexto and 1 <= dia <= 28):
            print("Data válida")
        else:
            print("Data inválida")
    elif mes in [4, 6, 9, 11]: 
        if 1 <= dia <= 30:
            print("Data válida")
        else:
            print("Data inválida")
    else:  
        if 1 <= dia <= 31:
            print("Data válida")
        else:
            print("Data inválida")
