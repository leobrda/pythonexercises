#Maneira tradicional
#co = float(input('Comprimento do cateto oposto: '))
#ca = float(input('Comprimento do cateto adjacente: '))
#hip = ((co ** 2) + (ca ** 2)) ** (1/2)
#print('A hipotenusa desse triângulo é de {:.2f}.'.format(hip))

#Importando biblioteca
#import math
#co = float(input('Comprimento do cateto oposto: '))
#ca = float(input('Comprimento do cateto adjacente: '))
#hip = math.hypot(co, ca)
#print('A hipotenusa desse triângulo é de {:.2f}.'.format(hip))

#Importando somente a função hypot
from math import hypot
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
hip = hypot(co, ca)
print('A hipotenusa desse triângulo é de {:.2f}.'.format(hip))
