d = int(input())
a = int(input())
n = int(input())
gasto = 0
if n >= 16:
  gasto = (32 - n) * (d + 14 * a)
else:
  gasto = (32 - n) * (d + (n - 1) * a)
print(gasto)
