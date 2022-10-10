def potencia(n):
  dec = 0
  p = 1
  while n > dec:
    dec = 10**p
    p += 1
    if n < dec:
      d = n - (dec//10)
      return d
    if n == dec:
      return 0
      
subtracoes = []
t = int(input())
for a in range(t):
  m = int(input())
  subtracoes.append(potencia(m))
for b in subtracoes:
  print(b)