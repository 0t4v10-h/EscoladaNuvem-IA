"""
Crie um script em Python que leia um arquivo CSV e exiba os dados na tela. O arquivo CSV deve conter informações de pessoas, com colunas Nome, Idade e Cidade.
"""
import pandas as pd

# Caminho do arquivo CSV
nome_arquivo = 'dados_pessoais.csv'

# Leitura do arquivo CSV
df = pd.read_csv(nome_arquivo)

# Exibir os dados
print("Dados carregados do arquivo CSV:\n")
print(df)