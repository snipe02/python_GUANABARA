"""Faça um programa que leia um ano qualquer e mostre se ela é BISSEXTO."""

from datetime import date
ano = int(input("em que analisar? Coloque o para analisar o ano atual: "))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0: # se ano for resto dividido por 4  igual 0  e tambem ano resto dividido
#por 100 diferente igual 0 or ano  resto dividido por 400 igual 0
    print(f"O ano {ano} é bissexto.")
else:
    print(f"O ano {ano} não é bissexto.")