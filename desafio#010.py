"""Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos Dólares
ela pode comprar. considera US$ 1,00 = R R$ 3,27 """

real = float(input("quanto dinheiro eu tenho na carteira? R$ "))
dola = real / 5.21
print(f'com R${real:.2f} voce pode comprar US${dola:.2f} ')