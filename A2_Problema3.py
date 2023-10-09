valor_hora = float(input("Digite o valor da hora de trabalho: ")
qnt_horas = int(input("Digite a quantida de horas trabalhadas nos mês: ")

salario = valor_hora * qnt_horas

def pagamento (IR, imposto)
  if salario <= 900
    imposto = 0
  elif salario <= 1500
    imposto = 0,05
  elif salario <= 2500
    imposto = 0,10
  else 
    imposto = 0,20

IR = salario * imposto
return IR

INSS = (salario * 0,10)
FGTS = (salario * 0,11)

desconto = IR + INSS

print("Salário Bruto: R$%.2f \nIR: %f \nINSS: %.2f\nFGTS: %.2F Total de descontos: %.2f \nSalário líquido: %.2f " % (salario, IR, INSS, FGTS, salario - desconto)
      
      





                
