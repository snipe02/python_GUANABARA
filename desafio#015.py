"""Escreva um programa que pergunta  a  quantidade de km percorido por um carro alugado e a quantidade de dias pelos
quias ela foi alugado. Calacule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado."""

dias = int(input("Quantos dias alugados "))
km = float(input(" Quantos km rodados "))
pagar = (dias * 60) + (km * 0.15)
print(f'O total a pagar è de R${pagar:.2f}')







