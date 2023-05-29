"""Cre  um progroma que leia um número Real qualquer pelo teclado e mostre na tela a sua porção inteiro."""

from math import trunc
num = float(input("Digite um numero: "))
print(f'o numero {num} tem a parte inteira {trunc(num)}')


