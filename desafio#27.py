"""Faça um programa que leia o nome completo de uma pessoa, mostrando em seguindo o
primeiro e o último nome separadamente.
Ex: Ana Maria de Souza
primeiro = Ana
ultimo = Souza """

nome = str(input("Digite seu nome clompleto: ")).strip()
pessoa = nome.split()

print(f'Seu primeiro nome é Pedro {pessoa[0]}')
print(f' seu ultomo nome è {pessoa[-1]}')