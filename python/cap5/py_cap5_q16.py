n, m, a, b = map(int, input().split())
gasto = 0
construir = 0
demolir = 0
if n % m != 0:
  if n > m:
    construir = a * (m - (n - m))
    demolir = b * (n - m)
    if construir < demolir:
      gasto += construir
    else:
      gasto += demolir
  else:
    construir = a * (m - n)
    demolir = b * (m - (m - n))
    if construir < demolir:
      gasto += construir
    else:
      gasto += demolir
print(gasto)