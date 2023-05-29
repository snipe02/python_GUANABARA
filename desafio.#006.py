"""cria um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada."""

n = int(input("digite um número: "))
d = n * 2
t = n * 3
r = n ** (1/2)
print(f' o dobro de {n} vale {d}')
print(f'o triplo de {n}  vale {t} \n a raiz quadrada de {n} é igual a {r:.0f}')

