segundos = input('Digite o valor do tempo em segundos: ')
segundos = int(segundos)

horas = segundos//3600
segundos %= 3600
minutos = segundos // 60
segundos %= 60


print(f"Valor convertido: {horas} h {minutos} min {segundos} s") 

