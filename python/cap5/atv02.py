print("Digite o valor da compra")
valor = float(input())
if valor >= 500.0:
  valor -= valor * 0.5
elif valor >= 400.0:
  valor -= valor * 0.4
elif valor >= 300.0:
  valor -= valor * 0.3
elif valor >= 200.0:
  valor -= valor * 0.2
elif valor >= 100.0:
  valor -= valor * 0.1
print(valor)