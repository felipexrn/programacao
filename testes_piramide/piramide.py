def piramide(n):
  #n = int(input())
  piramide = []
  
  h = n//2
  if n/2 > n//2:
    h += 1
  
  for i in range(n):
    camada = []
    for j in range(n):
      camada.append(1)
    piramide.append(camada)
  
  x = 0
  y = 0
  
  while h > 0:
    n -= 2
    for i in range(n):
      camada = piramide[i+1+y]
      for j in range(n):
        camada[j+1+y] += 1
    h -= 1
    x += 1
    y += 1
    
  #for i in piramide:
  #  print(*i)
  return piramide