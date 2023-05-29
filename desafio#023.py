"""faça um programa que leia um número do 0 a 9999 e mostre na tela a cada um dos digitos separados.
ex:
Digite um número: 1834
unidade:4 dezena: 3 centena:8 milhar:1"""
import math
numero = int(input("informe um numero : "))
u = numero // 1 % 10
d = numero // 10 % 10
c = numero // 100 % 10
m = numero // 1000 % 10
print(f'Analisando o numero {numero}')
print(f'Unidade: {u}')
print(f'Desena: {d}')
print(f'Centena: {c}')
print(f'milhar: {m}')