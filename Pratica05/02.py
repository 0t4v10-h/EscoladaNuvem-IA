"""
Crie uma função que verifique se uma palavra ou frase é um palíndromo (lê-se igual de trás para frente, ignorando espaços e pontuação). Se o resultado é True, responda “Sim”, se o resultado for False, responda “Não”.
"""

def eh_palindromo(frase):
    return frase == frase[::-1]  # Inverte a frase

frase = input("Digite uma frase: ")
if eh_palindromo(frase):
    print("Sim")
else:
    print("Nao")
    