"""desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não
formar um triãngulo."""
print("analisador de triangulo")
print('-='*20)
r1 = float(input("primeiro seguimento "))
r2 = float(input("segundo seguimento "))
r3 = float(input("terceiro seguimento "))
if r1 < r2 + 3 and r2 < r1 + r3 and r3 < r2 + r1: # se r1 for menor que r2 + r3  e r2 for menor que r1 etc....
    print('Os segmento acima PODEM FORMAR triângulo!')
else:
    print('os segmento acima NÃO PODEM triângulo')
