a = int(input())
b = int(input())
c = int(input())
if a + b > c and a + c > b and b + c > a:
  if a == b and a == c:
    print("equilátero")
  elif a != b and b != c:
    print("escaleno")
  else:
    print("isósceles")
else: 
  print("nenhum")