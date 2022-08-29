n = int(input())
s = int(input())
x = list(map(int, input().split()))
contador = 0
inicio = 0
intervalos = 0
for b in x:
  contador = 0
  for c in x:
    contador += 1
    sub = x[inicio:contador]
    soma = sum(sub)
    if soma == s:
      intervalos += 1
  inicio += 1
  contador = 0
print(intervalos)

"""
Entrada
6
2
0 2 0 1 0 1
Saída
6

Entrada
8
13
10 1 0 0 9 10 1 5
Saída
0

Entrada
5
6
1 0 3 0 2
Saída
1
"""