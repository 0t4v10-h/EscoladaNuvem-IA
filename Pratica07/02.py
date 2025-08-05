"""
Crie um script em Python que escreva dados em um arquivo CSV. O arquivo CSV deve conter informações pessoais, como colunas Nome, Idade e Cidade.
"""

import pandas as pd

# Dicionário com os dados
dados = {
    'Nome': ['Ana', 'Carlos', 'Marina', 'João'],
    'Idade': [25, 30, 22, 35],
    'Cidade': ['São Paulo', 'Rio de Janeiro', 'Belo Horizonte', 'Curitiba']
}

# Cria o DataFrame e salva como CSV
df = pd.DataFrame(dados)

# Salva o DataFrame em um arquivo CSV
df.to_csv('dados_pessoais.csv', index=False, encoding='utf-8')

print('Arquivo "dados_pessoais.csv" criado com sucesso!')
