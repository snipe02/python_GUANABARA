"""faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de  desconto."""

preço = float(input(" qual o preço de um produto "))
novo = preço-(preço*5/100)
print(f"o produto que custava R${preço:.2f}, na promoçao com desconto de  5% vai custar R$ {novo:.2f}")