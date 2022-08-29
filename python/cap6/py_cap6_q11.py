numeros = list(map(int, input().split()))
if len(numeros) % 2 == 0:
  metade = (len(numeros) // 2) - 1
  metade1 = numeros[metade]
  metade2 = numeros[metade + 1]
  print((metade1 + metade2) / 2)
else:
  print(numeros[len(numeros) // 2])
