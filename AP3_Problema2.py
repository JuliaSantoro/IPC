def pagamento(valor_hora, horas_trabalhadas):
    hora = float(valor_hora)
    trabalho = float(horas_trabalhadas)
    salario_bruto = hora * trabalhado
    
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
   return salario_liquido, desconto


   
