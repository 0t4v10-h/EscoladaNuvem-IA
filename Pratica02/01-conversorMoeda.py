"""
Crie um programa que converte um valor em reais para dólares e euros. Use os seguintes dados:



Valor em reais: R$ 100.00

Taxa do dólar: R$ 5.60

Taxa do euro: R$ 6.60 
O programa deve calcular e exibir os valores convertidos, arredondando para duas casas decimais.
"""

valor_reais = int(input("Digite o valor em reais: "))
taxa_dolar = 5.60
taxa_euro = 6.60

valor_dolar = round((valor_reais / taxa_dolar), 2)
valor_euro = round((valor_reais / taxa_euro), 2)

print("\nValor em reais:", valor_reais)
print("Taxa do dolar:", taxa_dolar)
print("Taxa do euro:", taxa_euro)
print("Valor em dolar:", valor_dolar)
print("Valor em euro:", valor_euro)