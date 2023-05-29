"""Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todos as infromaões possives sobre
ela."""
a = input("digite algo")
print(f"o tipo primitivo " , type(a))
print(' so tem espaços? ' , a.isspace())
print('è um numero? ' , a.isnumeric())
print(' é alfabetico?' , a.isalpha())
print('é alfa numerico?' , a.isalnum())
print(' está  em  maiùscula?' ,a.isupper())
print(' está em minusculas?' ,a.islower())
print(' está capitalizada?' ,a.istitle())