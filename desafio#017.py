"""faça um programa que leia o comprimento do canteto oposto e do cateto adjacendo de um
triangulo retãngulo, calcule e mostre o comprimento do hipotenusa."""

#comp = float(input('comprimento oposto: '))
#adje = float(input('comprimento de ajacendo: '))
#hi = (comp ** 2 + adje ** 2) ** (1/2) 
#print(f'A hipotenusa vai medir {hi:.2f}')

from math import hypot
comp = float(input('comprimento oposto: '))
adje = float(input('comprimento de ajacendo: '))
hi = hypot(comp, adje)
print(f'A hipotenusa vai medir {hi:.2f}')
