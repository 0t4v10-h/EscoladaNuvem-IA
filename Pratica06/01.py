"""
Crie um programa que gera uma senha aleatória com o módulo random, utilizando caracteres especiais, possibilitando o usuário a informar a quantidade de caracteres dessa senha aleatória.
"""

import random
import string

def gerar_senha(tamanho):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    senha = ''.join(random.choice(caracteres) for _ in range(tamanho))
    return senha

def main():
    try:
        tamanho = int(input("Digite o número de caracteres da senha: "))
        if tamanho <= 0:
            print("O tamanho deve ser maior que zero.")
        else:
            senha = gerar_senha(tamanho)
            print(f"Senha gerada: {senha}")
    except ValueError:
        print("Por favor, digite um número inteiro válido.")

if __name__ == "__main__":
    main()