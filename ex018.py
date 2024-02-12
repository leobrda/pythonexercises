#import math
#ang = float(input('Digite o ângulo desejado: '))
#x = math.radians(ang)
#seno = math.sin(x)
#cosseno = math.cos(x)
#tangente = math.tan(x)
#print('O ângulo de {} graus tem o SENO de {:.2f}.'.format(ang, seno))
#print('O ângulo de {} graus tem o COSSENO de {:.2f}.'.format(ang, cosseno))
#print('O ângulo de {} graus tem o TANGENTE de {:.2f}.'.format(ang, tangente))

from math import radians, sin, cos, tan
ang = float(input('Digite o ângulo desejado: '))
x = radians(ang)
seno = sin(x)
cosseno = cos(x)
tangente = tan(x)
print('O ângulo de {} graus tem o SENO de {:.2f}.'.format(ang, seno))
print('O ângulo de {} graus tem o COSSENO de {:.2f}.'.format(ang, cosseno))
print('O ângulo de {} graus tem o TANGENTE de {:.2f}.'.format(ang, tangente))
