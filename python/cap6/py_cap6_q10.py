numeros = list(map(int, input().split()))
if sum(numeros) % len(numeros) == 0:
  print("Sim")
else:
  print("Nao")
