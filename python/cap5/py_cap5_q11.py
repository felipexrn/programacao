a = int(input())
b = int(input())
c = int(input())
if a <= b and b <= c:
  if a + b > c:
    print("maior")
  else:
    print("não maior")
elif a <= b and c <= b:
  if a + c > b:
    print("maior")
  else:
    print("não maior")
elif b <= a and c <= a:
  if b + c > a:
    print("maior")
  else:
    print("não maior")