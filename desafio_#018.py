"""faça um programa que leia ângulo qualquer e mostre na tela o valor do seno conseno e
tangente desse ângolo."""

from math import radians,sin,cos,tan
angulo = float(input("Digite o angulo que você deseja: "))
seno = sin(radians( angulo))
cose = cos(radians(angulo))
tang = tan(radians(angulo))
print(f'o angulo de {angulo} tem  o SENO de {seno:.2f}\nO angulo de {angulo:.2f} tem o COSSENO de {seno:.2f}\nO angulo de {angulo:.2f} tem a TAGENTE de {tang:.2f}')

