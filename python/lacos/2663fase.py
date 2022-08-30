n = int(input())
k = int(input())
p = []

for i in range(n):
  p.append(int(input()))

p.sort()
p.reverse()
ultimo = p[k-1]
p.reverse()
p = p[p.index(ultimo):]

print(len(p))