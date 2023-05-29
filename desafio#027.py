"""Faça um programa que leia o nome completo de uma pessoa, mostrando em seguindo o
primeiro e o último nome separadamente.
Ex: Ana Maria de Souza
primeiro = Ana
ultimo = Souza """

nome = str(input("Digite seu nome completo: ")).strip()
pessoa = nome.split()
print(f'Seu primeiro nome é {pessoa[0]}')
print(f' seu ultimo nome é {pessoa[-1]}')
