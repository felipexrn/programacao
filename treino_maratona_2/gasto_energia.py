l, c = map(int, input().split())
consumo = list(map(int, input().split()))
maximos = []
consumo.sort()
for i in range(l):
  para = False
  maximo = consumo[i]
  for j in range(l):
    if i != j:
      if maximo <= c:
        maximo += consumo[j]
      if maximo > c:
        maximo -= consumo[j]
        if maximo < min(consumo):
          maximo = 0
          para = True
          break
  maximos.append(maximo)
  if para:
    break
print(max(maximos))