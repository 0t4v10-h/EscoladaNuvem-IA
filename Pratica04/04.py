"""
Crie um programa que solicite ao usuário que insira números inteiros. O programa deve continuar solicitando números até que o usuário digite 'fim'. Para cada número inserido, o programa deve informar se é par ou ímpar. Se o usuário inserir algo que não seja um número inteiro, o programa deve
informar o erro e continuar. No final, o programa deve exibir a quantidade de números pares e ímpares inseridos.
"""

numeros_pares = 0
numeros_impares = 0

while True:
    numero = input("Digite um número (ou 'fim' para encerrar): ")
    if numero == 'fim':
        break
    try:
        numero = int(numero)
        if numero % 2 == 0:
            numeros_pares += 1
            print(f"{numero} é par.")
        else:
            numeros_impares += 1
            print(f"{numero} é impar.")
    except ValueError:
        print("Entrada inválida. Digite novamente.")

print(f"Quantidade de números pares: {numeros_pares}")
print(f"Quantidade de números impares: {numeros_impares}")