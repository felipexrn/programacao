n = int(input())
x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())
metade = n // 2
quadrante1 = x1 > metade and x2 > metade and y1 <= metade and y2 <= metade
quadrante2 = x1 <= metade and x2 <= metade and y1 <= metade and y2 <= metade
quadrante3 = x1 <= metade and x2 <= metade and y1 > metade and y2 > metade
quadrante4 = x1 > metade and x2 > metade and y1 > metade and y2 > metade
if quadrante1 or quadrante2 or quadrante3 or quadrante4:
  print("N")
else:
  print("S")