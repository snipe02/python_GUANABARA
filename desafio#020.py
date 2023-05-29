"""O mesmo professor do desafio anterior quer sortear a ordem de apresenração de trabalhos dos alunos. faça um programa
que leia o nome dos quatro alunos e mostre a ordem sorteado."""

from random import shuffle
n1 = input("nome do auno: ")
n2 = input("nome do auno: ")
n3 = input("nome do auno: ")
n4 = input("nome do auno: ")
lista = [n1,n2,n3,n4]
shuffle(lista)
print(f'os nomes sorteados ção{lista}')
