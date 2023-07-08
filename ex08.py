"""Converta a distancia de metros para kilometros decametros e milimetros e centimetros"""

n1 = float(input("Digite aqui sua distância em Métros: "))
print(f"a distacia {n1} M em km equivale a {(n1*1000):.0f} \nem centimetros {(n1/100)} \nem decametros {(n1/10):.0f} \nem milimetros {n1/1000}")
