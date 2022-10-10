while True:
  d = []
  e = []
  total_pares = 0
  for i in range(30,61):
    d.append(0)
    e.append(0)
  try:
    n = int(input())
    for i in range(n):
      m, l = input().split()
      m = int(m)
      if l == "E":
        e[m-30] += 1
      else:
        d[m-30] += 1
    for i in range(len(d)):
      if d[i] > 0 and e[i] > 0:
        pares = (d[i] + e[i]) // 2
        total_pares += pares
    print(total_pares)
  except:
    break