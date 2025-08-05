"""
Crie um script em Python que leia e escreva dados em um arquivo JSON. O arquivo JSON deve conter informações de uma pessoa, com campos nome, idade e cidade.
"""

import json

pessoa = {
    "nome": "Ana",
    "idade": 25,
    "cidade": "São Paulo"
}

arquivo_json = 'pessoa.json'

# Escrevendo os dados no arquivo json
with open(arquivo_json, 'w', encoding='utf-8') as f:
    json.dump(pessoa, f, ensure_ascii=False, indent=4)

print(f'Dados escritos no arquivo "{arquivo_json}".')

# Lendo os dados do arquivo json
with open(arquivo_json, 'r', encoding='utf-8') as f:
    dados = json.load(f)

print("\nDados lidos do arquivo JSON: ")
print(dados)