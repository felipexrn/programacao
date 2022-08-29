numeros = list(map(int, input().split()))
if sum(numeros) % 2 == 0:
  print("Par")
else:
  print("Impar")
