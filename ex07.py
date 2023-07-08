"""Calcule a média da nota do aluno."""

name = input("Digite seu nome: ")
nota1 = float(input("Digite sua primeira nota: "))
nota2 = float(input("Digite a sua segunda nota: "))
nota3 = float(input("Digite a sua terceira nota: "))
print(f"aluno {name}, sua média foi de {((nota1 + nota2 + nota3) /3):.2f}")
