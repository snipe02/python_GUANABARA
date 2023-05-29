"""faça um programa que leia uma frase pela teclado e mostre.
Quantas vezes aparece a letra "A"
em que posição ela aparece a primeira vez.
em que posição ela aparece a útima vez."""

nome = str(input("Digite uma frase:  ")).upper().strip()
letra = nome.count("A")
leta = nome.find("A")
le = nome.rfind("A")
print(f'A letra A aparece {letra} vezes na frase.')
print(f'A primeira letra A aparece na posisão {leta+1}')
print(f'A útima letra A aparece na posição {le+1}')

