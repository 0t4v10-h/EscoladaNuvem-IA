"""
Calculadora de Volume

Crie um programa que calcule o volume de uma caixa retangular. Use as seguintes dimensões:
Comprimento: 12 cm
Largura: 14 cm
Altura: 20 cm O programa deve calcular o volume e exibir o resultado em cm³.
"""

comprimento = input("Digite o comprimento da caixa (em cm): ")
largura = input("Digite a largura da caixa (em cm): ")
altura = input("Digite a altura da caixa (em cm): ")

comprimento = float(comprimento)
largura = float(largura)
altura = float(altura)

volume = comprimento * largura * altura

print("O volume da caixa e:", volume, "cm^3")