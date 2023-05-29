"""Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5 epeça para o usuário
tentar descobrir qual foi o número escolhido pelo computador.
O programa deverá escrever na tela se o usuário venceu ou perdeu"""

from random import  randint
from time import sleep
computador = randint(0, 5) # fazer o computador pensar
print('-=-' *20)
print('vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=-' *20)
jogador = int(input('Em que número eu pensei? ')) # jogador tenta adivinhar
print("PROCESANDO...")
sleep(3)
if jogador == computador:
    print('PARABENS! Você conseguiu me vencer!')
else:
    print(f'GANHEI! Eu pensei no número {jogador} e não no {computador}')