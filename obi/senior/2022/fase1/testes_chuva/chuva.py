def int_chuva(n, s, x):
  #n = int(input())
  #s = int(input())
  #x = list(map(int, input().split()))
  intervalos = 0
  for a in range(n):
    soma = 0
    for b in range(a,n):
      soma = soma + x[b]
      if soma == s: intervalos += 1
      if soma > s: break
  return intervalos

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