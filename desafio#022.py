"""Crie um programa que leia o nome completo de uma pessoa e mostre :
 -> O nome com todos as letras maiusculos e minúsculos.
 -> Quantos letras ao todos(sem considerar espaços).
 -> quantas letras tem o primeiro nome."""

nome = input('Digite seu nome :  ').strip()
print(f'Analisando seu nome...\nSeu nome em maiuscula é {nome.upper()}')
print(f'Seu nome em minusculo é {nome.lower()}')
print(f'Seu nome tem ao todo {len(nome)} letras')
print(f'Seu primeiro nome tem {nome.find() } letras ')

