"""
Crie um programa que consulte a cotação atual de uma moeda estrangeira em relação ao Real Brasileiro (BRL). O usuário deve informar o código da moeda desejada (ex: USD, EUR, GBP), e o programa deve exibir o valor atual, máximo e mínimo da cotação, além da data e hora da última atualização. Utilize a API da AwesomeAPI para obter os dados de cotação.
"""

import requests

moeda = input("Digite o código da moeda: ")

url = f"https://economia.awesomeapi.com.br/json/last/{moeda}-BRL"

try:
    resposta = requests.get(url)
    resposta.raise_for_status()

    dados = resposta.json()
    cotacao_atual = dados[f"{moeda}BRL"]["bid"]
    cotacao_maxima = dados[f"{moeda}BRL"]["high"]
    cotacao_minima = dados[f"{moeda}BRL"]["low"]
    data_hora_atualizacao = dados[f"{moeda}BRL"]["create_date"]

    print(f"Cotação atual: {cotacao_atual}")
    print(f"Cotação máxima: {cotacao_maxima}")
    print(f"Cotação mínima: {cotacao_minima}")
    print(f"Data e hora da atualização: {data_hora_atualizacao}")

except requests.exceptions.RequestException as e:
    print("Erro ao se conectar à API:", e)

except KeyError as e:
    print("Erro ao processar os dados da cotação:", e)

except Exception as e:
    print("Erro desconhecido:", e)

except:
    print("Erro desconhecido.")

finally:
    print("Fim do programa.")
    