"""
Crie um programa que gera um perfil de usuário aleatório usando a API 'Random User Generator'. O programa deve exibir o nome, email e país do usuário gerado.
"""

import requests

def gerar_usuario():
    url = "https://randomuser.me/api/"
    try:
        resposta = requests.get(url)
        resposta.raise_for_status()  

        dados = resposta.json()
        usuario = dados['results'][0]

        nome = f"{usuario['name']['first']} {usuario['name']['last']}"
        email = usuario['email']
        pais = usuario['location']['country']

        print("=== Perfil de Usuário Gerado ===")
        print(f"Nome:  {nome}")
        print(f"Email: {email}")
        print(f"País:  {pais}")

    except requests.exceptions.RequestException as e:
        print("Erro ao se conectar à API:", e)
    except (KeyError, IndexError) as e:
        print("Erro ao processar os dados do usuário:", e)

if __name__ == "__main__":
    gerar_usuario()

