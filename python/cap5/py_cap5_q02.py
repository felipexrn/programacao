a, b, c = map(int, input().split())
if (a < b and a < c):
  print("A")
elif (b > c):
  print("B")
else:
  if (c < a or a + b < c):
    print("C")
  else:
    print("D")