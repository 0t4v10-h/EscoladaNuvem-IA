"""
Crie um programa que receba o preço original de um produto e um percentual de desconto, realizando o cálculo do preço final após a aplicação do desconto. Requisitos:
Permitir que o usuário informe o preço do produto e o percentual de desconto.
Utilizar operações matemáticas para calcular o valor do desconto e o preço final.
Exibir o preço final com duas casas decimais para garantir precisão. Entrada esperada: preço do produto (exemplo: 250.75) e o percentual de desconto (exemplo: 10).
"""

preco = float(input("Digite o preco do produto: "))
desconto = float(input("Digite o percentual de desconto: "))

preco_final = preco * (1 - desconto / 100)

print(f"Preco final: R$ {preco_final:.2f}")
