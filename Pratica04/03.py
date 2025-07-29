"""
Crie um programa que verifique se uma senha é forte. Uma senha forte deve ter pelo menos 8 caracteres e conter pelo menos um número. O programa deve continuar pedindo senhas até que uma válida seja inserida ou o usuário digite 'sair'.
"""

while True:
    senha = input("Digite uma senha: ")
    if senha == "sair":
        break
    if len(senha) < 8:
        print("A senha deve ter pelo menos 8 caracteres.")
    elif not any(char.isdigit() for char in senha):
        print("A senha deve conter pelo menos um número.")
    else:
        print("Senha forte!")
        break