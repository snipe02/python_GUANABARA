"""Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome."""

nome = str(input('qual seu nome completo?  ')).strip()
no = "silva" in nome.lower()
print(f'Seu nome tem Silva?{nome} {no}')
