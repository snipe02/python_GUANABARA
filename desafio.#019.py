"""Um professor quer sortear um dos seus quatro alunos para apagar o quadro. faça um programa que ajuda ele,
lendo o nome deles e  escrevendo o nome do escolhido"""

from random import choice
n1 = strinput(" primeiro aluno: ")
n2 = input("segundo aluno: ")
n3 = input("terceiro aluno: ")
n4 = input("quarto aluno : ")
lista = [n1,n2,n3,n4]
escolhido = choice(lista) #random.choice
print(f'escolhido foiano: {escolhido}')