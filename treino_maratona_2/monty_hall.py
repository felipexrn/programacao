n = int(input())
conquistas = 0
for i in range(n):
  if int(input()) != 1:
    conquistas += 1
print(conquistas)