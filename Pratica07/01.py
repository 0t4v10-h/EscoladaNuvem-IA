"""Leia um arquivo que contenha dados de log de treinamento de modelos de Machine Learning. Calcule a média e o desvio padrão do tempo de exercução constantes.
"""

import pandas as pd
import re

# Caminho do arquivo de log
caminho_log = 'log_treinamento.txt'

# Lista para armazenar os tempos extraídos
tempos_execucao = []

# Lê o arquivo linha por linha
with open(caminho_log, 'r', encoding='utf-8') as arquivo:
    for linha in arquivo:
        # Expressão regular para encontrar o tempo em segundos
        match = re.search(r'Tempo de execução:\s*([\d.]+)s', linha)
        if match:
            tempo = float(match.group(1))
            tempos_execucao.append(tempo)

# Converte para DataFrame
df = pd.DataFrame(tempos_execucao, columns=['Tempo (s)'])

# Cálculo da média e desvio padrão
media = df['Tempo (s)'].mean()
desvio_padrao = df['Tempo (s)'].std()

# Exibe resultados
print(f"Média do tempo de execução: {media:.2f} segundos")
print(f"Desvio padrão do tempo de execução: {desvio_padrao:.2f} segundos")
