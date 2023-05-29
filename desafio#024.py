"""Crie um programa que leia o nome de uma cidade e diga se ela começo ou não com o nome"SANTO." """

cid = str(input(" em que cidade voçê nasceu: ")).strip()
print(cid[:5].upper() == 'SANTO')