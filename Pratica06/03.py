"""
Desenvolva um programa que consulte informações de endereço a partir de um CEP fornecido pelo usuário, utilizando a API ViaCEP. O programa deve exibir o logradouro, bairro, cidade e estado correspondentes ao CEP consultado.
"""

import requests

cep = input("Digite o CEP: ")

url = f"https://viacep.com.br/ws/{cep}/json/"
try:
    resposta = requests.get(url)
    resposta.raise_for_status()

    dados = resposta.json()
    logradouro = dados["logradouro"]
    bairro = dados["bairro"]
    cidade = dados["localidade"]
    estado = dados["uf"]

    print(f"Logradouro: {logradouro}")
    print(f"Bairro: {bairro}")
    print(f"Cidade: {cidade}")
    print(f"Estado: {estado}")

except requests.exceptions.RequestException as e:
    print("Erro ao se conectar à API:", e)