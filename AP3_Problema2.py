def pagamento(valor_hora, horas_trabalhadas):
    salario_bruto = valor_hora * horas_trabalhadas
    
    if salario_bruto <= 900:
        desconto_ir = 0
    elif salario_bruto <= 1500:
        desconto_ir = 5
    elif salario_bruto <= 2500:
        desconto_ir = 10
    else:
        desconto_ir = 20
    
    desconto = (salario_bruto * desconto_ir) / 100
    salario_liquido = salario_bruto - desconto
    
    print("Salário bruto: {:.2f}".format(salario_bruto))
    print("Desconto: {:.2f}".format(desconto))
    print("Salário líquido: {:.2f}".format(salario_liquido))
    return salario_liquido
