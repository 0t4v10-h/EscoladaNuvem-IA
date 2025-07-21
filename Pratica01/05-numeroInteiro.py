"""
Calculadora de Número Inteiro
Leia quatro valores inteiros A, B, C e D. A seguir, calcule e mostre a diferença do produto de A e B pelo produto de C e D segundo a fórmula: DIFERENCA = (A * B - C * D).
Entrada: O arquivo de entrada contém 4 valores inteiros. 
Saída: Imprima a mensagem "DIFERENCA = " com todas as letras maiúsculas.
"""

A = int(input("Valor de A: "))
B = int(input("Valor de B: "))
C = int(input("Valor de C: "))
D = int(input("Valor de D: "))

DIFERENCA = (A * B - C * D)

print("DIFERENCA =", DIFERENCA)