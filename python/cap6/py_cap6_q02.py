numeros = list(map(int, input().split()))
a0 = numeros[0]
a1 = numeros[1]
numeros[0] = a1
numeros[1] = a0
print(*numeros)
