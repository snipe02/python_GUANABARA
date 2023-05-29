"""faça um algoritmo que leia o salario de um fucionario e mostre seu novo salário, com 15% de aumento."""
salario = float(input("mostre seu salario R$ "))
novo = salario + (salario * 15 / 100) #15% duvudido por 100
print(f"um fucionario que ganhava R${salario:.2f}, com 15% de aumento, passa a receber R${novo:.2f}")