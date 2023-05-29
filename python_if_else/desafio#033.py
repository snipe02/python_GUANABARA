"""Faça um programa que leia três números emostre qual é o maior e qual é o menor."""
# num = int(input(' pirmeiro valor: '))
# segundo = int(input('Segundo valor: '))
# terc = int(input('Terceiro valor'))
# nume = max(num,segundo,terc)
# print(f'{nume}')

3

a = int(input('pirmeiro valor: '))
b  = int(input('Segundo valor: '))
c = int(input('Terceiro valor: '))
menor = a
if a < b and a < c:  # se a menor que b é a ,menor que c
    menor = a
if b < c and b < a:
    menor = b
if c < a and c < b:
    menor = c

maior = a
if  a > b and a > c:
    maior = a
if b > a and b > c:
    maior = b
if c > b and c > a:
    maior = c
print(f'numero menor é : {menor}')
print (f'numero maior é : {maior}')