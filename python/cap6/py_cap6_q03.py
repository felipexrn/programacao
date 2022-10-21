numeros = list(map(int, input().split()))
if len(numeros) > 4:
  numeros = numeros[:5]
print(numeros[0], numeros[4])
