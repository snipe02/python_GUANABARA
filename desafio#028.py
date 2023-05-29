"""Escreva  um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o
usuàrio tentar descobrir qual foi o numero escolhido pelo computador.
O programa deverá escrever  na tela se o usuario venceu ou perdeu."""

from random import randint
from time import sleep
computador = randint(0, 5)  #faz o computador pensar
print('=--=' *20)
print("vou pensar em um número entre 0 e 5. tente adivinhar... ")
print('=--=' *20)
numero = int(input("em que número eu pensei? "))   #numero tentar adivinhar
print("procesando...")
sleep(3)
if computador == numero:   #se o compotador for igual ao numero
    print('PARABÉNS! Você conseguiu me vencer!')
else:
    print(f"GANHEI! eu pensei no número {computador} e não {numero}")