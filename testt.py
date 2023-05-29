codigo = int(input("Digite o código do produto: "))
quantidade = int(input("Digite a quantidade do produto: "))

if codigo == 1:
    preco_unitario = 4.00
elif codigo == 2:
    preco_unitario = 4.50
elif codigo == 3:
    preco_unitario = 5.00
elif codigo == 4:
    preco_unitario = 2.00
elif codigo == 5:
    preco_unitario = 1.50
else:
    print("Código inválido. Tente novamente.")
    exit()

valor_total = quantidade * preco_unitario

print(f"Total: R$ {valor_total:.2f}")
