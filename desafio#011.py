"""faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade
de tinta  necessário para pinta-lo, sabendo que cada litro de tinta,pinta uma área de 2m²."""

largura = float(input("a largura da parede é "))
altura = float(input("a altura da parede é "))
area = largura * altura
print(f'a sua parede tem a dimensão de {largura}x{altura} e a sua area é de {area}m²')
tinta = area / 2
print(f'para pintar essa parede, você precisará de {tinta}l de tinta')