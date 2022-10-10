a,b,c = map(int,input().split())
x,y,z = map(float,input().split())
if (a*y<b*x and a+b<=c):
  print("A")
elif (a+b<c or x/y<z):
  print("B")
else:
  if (a+c<b and x>y or z>y):
    print("C")
  else:
    print("D")
if (a+b+c>50 and x*y*z>1000):
  print("E")
else:
  print("F")
print("G")