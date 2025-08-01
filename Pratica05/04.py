"""
Crie uma função que calcule a idade de uma pessoa em dias, baseada no ano de nascimento.
"""

def calcular_idade_em_dias(ano_nascimento):
    idade_em_dias = (2025 - ano_nascimento) * 365
    return idade_em_dias

ano_nascimento = int(input("Digite o ano de nascimento: "))
idade_em_dias = calcular_idade_em_dias(ano_nascimento)
print(f"Idade em dias: {idade_em_dias}")
