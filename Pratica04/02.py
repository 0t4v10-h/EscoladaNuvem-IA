"""
Crie um programa que permita a um professor registrar as notas de uma turma. O programa deve continuar solicitando notas até que o professor digite 'fim'. Notas válidas são de 0 a 10. O programa deve ignorar notas inválidas e continuar solicitando. No final, deve exibir a média da turma.
"""

notas = []
soma = 0

while True:
    nota = input("Digite a nota (ou 'fim' para encerrar): ")
    if nota == 'fim':
        break
    try:
        nota = float(nota)
        if 0 <= nota <= 10:
            notas.append(nota)
            soma += nota
        else:
            print("Nota inválida. Digite novamente.")
    except ValueError:
        print("Entrada inválida. Digite novamente.")

if notas:
    media = soma / len(notas)
    print(f"Média da turma: {media:.2f}")
else:
    print("Nenhuma nota foi registrada.")