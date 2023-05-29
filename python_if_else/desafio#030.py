"""Crie um programa que leia um número inteiro é mostre na tela se ele é PAR ou IMPAR."""
numero = int(input("me dica um numero qulaquer: "))
if numero % 2 == 0: # se numero  for resto da divião por 2 é  igual a 0
    print(f" o {numero} é par")
else:
    print(f" o {numero} é impar")
