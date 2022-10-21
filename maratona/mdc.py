import math

t = int(input())

for i in range(t):
  n, l, r = map(int, input().split())
  lista = list(range(l, r+1))
  distinto = True
  mdc = []
  for a in lista:
    mdcN = math.gcd(lista.index(a)+1, a)
    mdc.append(mdcN)
    contador = 0
    #print(mdc)
    for b in mdc:
      if mdcN == b:
        contador += 1
        if contador == 2:
          distinto = False
    if not distinto:
      print('no')      
          
if distinto:
  print("yes")
  print(mdc)

"""
4
5 1 5
9 1000 2000
10 30 35
1 1000000000 1000000000

"""