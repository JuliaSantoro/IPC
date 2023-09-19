raio = input('Digite o valor do raio da circunferência: ')
raio = float(raio)

pi = 3.1415

perimetro = 2*pi*raio 

area = pi*raio**2

volume = 4*pi*((raio**3)/3)

print('Perímetro: %.2f \nÁrea: %.2f \nVolume: %.2f' % (perimetro, area, volume))
