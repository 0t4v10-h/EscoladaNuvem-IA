"""
Crie um programa que converta temperaturas entre Celsius, Fahrenheit e Kelvin. 

O usuário deve informar a temperatura, a unidade de origem e a unidade para qual deseja converter.
"""

temperatura = float(input("Digite a temperatura: "))
unidade_origem = input("Digite a unidade de origem (C, F ou K): ")
unidade_destino = input("Digite a unidade para qual deseja converter (C, F ou K): ")

if unidade_origem == "C":
    if unidade_destino == "F":
        temperatura = (temperatura * 9/5) + 32
    elif unidade_destino == "K":
        temperatura = temperatura + 273.15
elif unidade_origem == "F":
    if unidade_destino == "C":
        temperatura = (temperatura - 32) * 5/9
    elif unidade_destino == "K":
        temperatura = (temperatura - 32) * 5/9 + 273.15
elif unidade_origem == "K":
    if unidade_destino == "C":
        temperatura = temperatura - 273.15
    elif unidade_destino == "F":
        temperatura = (temperatura - 273.15) * 9/5 + 32

print(f"{temperatura:.2f} {unidade_destino}")