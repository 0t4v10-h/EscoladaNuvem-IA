"""
Desenvolva um programa que calcula o desconto em uma loja. Use as seguintes informações:

Nome do produto: "Camiseta"

Preço original: R$ 50.00

Porcentagem de desconto: 20% 
O programa deve calcular o valor do desconto e o preço final, exibindo todos os detalhes.
"""

nome_produto = "Camiseta"
preco_original = 50.00
porcentagem_desconto = 20

desconto = (preco_original * porcentagem_desconto) / 100
preco_final = preco_original - desconto

print("Produto:", nome_produto)
print("Preço original:", preco_original)
print("Porcentagem de desconto:", porcentagem_desconto)
print("Desconto:", desconto)
print("Preço final:", preco_final)