velocidade = input('Digite o valor da velocidade: ')
velocidade = float(velocidade)

aceleracao = input('Digite o valor da aceleração: ') 
aceleracao = float(aceleracao) 

tempo = input('Digite o valor do tempo: ')
tempo = float(tempo)

velocidade_final = velocidade + aceleracao * tempo 
distancia = velocidade * tempo + ((aceleracao * tempo **2)/2)

print('Velocidade final: %.2f \nDistância percorrida: %.2f' % (velocidade_final, distancia))
