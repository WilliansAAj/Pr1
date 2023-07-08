"""Operações aritimeticas"""

"""+soma, -subtração, *multiplicação, /divisão, **potenciação, //divisão inteira, %resto da divisão, x**(1/2) raiz quadrada"""
"""Ordem de precedência: 1º ()  n2º ** 3º /, //, % 4º+- """

n1 = float(input("Digite seu numero aqui:"))
n2 = float(input("Digite um segundo numero :"))
g = n1 + n2
a = n1 - n2
b = n1 * n2
c = n1 / n2
d = n1 ** n2
e = n1 // n2
f = n1 % n2
print(f"resultados {a} {b} {c} {d} {e} {f} {g}")
