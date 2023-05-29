"""Escreva um programa que leia a velocidade de um carro.
Se ele ultrapassar 80KM/h, mostrar uma mensagem dizendo que ele foi multado.
A multa vai custar R$7,00 por cada km acima do limite."""

velocidade = float(input("qual é a velocidade atual do carro? "))
if velocidade >  80: # se a velocidade for maior que 80
    print("MULTADO! Você excendeu o limite permitido que é de 80Km/h")
    multa = (velocidade - 80) * 7
print(f" Você deve pegar uma multa de R${multa}!")
print("Tenha um bom dia! Dirija com segurança!")
