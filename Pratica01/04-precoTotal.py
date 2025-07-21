"""
Calculadora de Preço Total

Desenvolva um programa que calcule o preço total de uma compra. Use as seguintes informações:

Nome do produto: "Cadeira Infantil"
Preço unitário: R$ 12.40
Quantidade: 3 
O programa deve calcular o preço total e exibir todas as informações, incluindo o resultado final.
"""

nome_produto = "Cadeira Infantil"
preco_unitario = 12.40

print("Produto:", nome_produto)
print("Preço:", preco_unitario)

quantidade = int(input("\nDigite a quantidade: "))
quantidade = int(quantidade)
preco_total = preco_unitario * quantidade

print("\nDetalhes da compra:")
print("Nome do produto:", nome_produto)
print("Preço unitário:", preco_unitario)
print("Quantidade:", quantidade)
print("Preço total:", preco_total)