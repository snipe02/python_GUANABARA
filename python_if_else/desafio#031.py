"""Desenvolva um programa que pergunte a distância de uma viagem em km. calcule o preço da passagem,
cobrando R$0,50 por Km para viagem de até 200km e R$0,45 para viagens mais longas."""

distancia = float(input("qual e a distancia da sua viagem? "))
print(f'voce esta prestes a começar uma viagem de R${distancia:.0f}.0km. ')
# preco = distancia * 0.50
# viagem = distancia * 0.45
if distancia <= 200: # se distancia for menor ou igual a 200:
    preco = distancia * 0.50

else:  #se não
    preco = distancia * 0.45

print(f'E o preço da sua passagem será de R${preco:.2f}')
