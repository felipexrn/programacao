t  = int(input())
campos = []
for a in range(t):
  linha1 = list(map(int, input().split()))
  linha2 = list(map(int, input().split()))
  campos.append([linha1, linha2])

for b in campos:
  if sum(b[0]) == 0 and sum(b[1]) == 0:
    print(0)
  elif sum(b[0]) == 2 and sum(b[1]) == 2:
    print(2)
  else:
    print(1)