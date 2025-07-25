"""
Desenvolva um programa que calcule o Índice de Massa Corporal (IMC) de uma pessoa.
O programa deve solicitar o peso (em kg) e a altura (em metros) do usuário,
calcular o IMC e fornecer a classificação de acordo com a tabela padrão de IMC.


< 18.5: classificacao = "Abaixo do peso" 

< 25: classificacao = "Peso normal"

 < 30: classificacao = "Sobrepeso"

 Para os demais cenários: classificacao = "Obeso"

"""

try:
    peso = float(input("Digite o peso (kg): "))
    altura = float(input("Digite a altura (m): "))

    if peso <= 0 or altura <= 0:
        print("Peso e altura devem ser maiores que zero.")
    else:
        imc = peso / (altura ** 2)
        print(f"Seu IMC é: {imc:.2f}")

        if imc < 18.5:
            print("Classificação: Abaixo do peso")
        elif imc < 25:
            print("Classificação: Peso normal")
        elif imc < 30:
            print("Classificação: Sobrepeso")
        else:
            print("Classificação: Obeso")

except ValueError:
    print("Entrada inválida. Por favor, insira números válidos.")
