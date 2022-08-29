numeros = list(map(int, input().split()))
if len(numeros) > 8:
  numeros = numeros[:8]
a0 = numeros[0]
a8 = numeros[7]
numeros[0] = a8
numeros[7] = a0
print(*numeros)
