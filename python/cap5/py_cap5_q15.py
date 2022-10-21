a, b = map(int, input().split())
if a == b:
  print(0)
elif a > b:
  if (a - b) % 2 == 0:
    print(1)
  elif (a - b) % 2 != 0:
    print(2)
else:
  if (b - a) % 2 == 0:
    print(2)
  else:
    if (b - a) % 2 != 0:
      print(1)