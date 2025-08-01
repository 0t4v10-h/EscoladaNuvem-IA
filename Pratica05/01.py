"""
Crie uma função que calcule a gorjeta a ser deixada em um restaurante, baseada no valor total da conta e na porcentagem de gorjeta desejada. Calcula o valor da gorjeta baseado no total da conta e na porcentagem desejada.
Parâmetros: valor_conta (float): O valor total da conta porcentagem_gorjeta (float): A porcentagem da gorjeta (ex: 15 para 15%)
Retorna: float: O valor da gorjeta calculada
"""

def calcular_gorjeta(valor_conta, porcentagem_gorjeta):
    gorjeta = valor_conta * (porcentagem_gorjeta / 100)
    return gorjeta  

valor_conta = float(input("Digite o valor da conta: "))
porcentagem_gorjeta = float(input("Digite a porcentagem da gorjeta: "))

gorjeta = calcular_gorjeta(valor_conta, porcentagem_gorjeta)

print(f"O valor da gorjeta é: R$ {gorjeta:.2f}")
print(f"O valor total da conta com gorjeta é: R$ {valor_conta + gorjeta:.2f}")