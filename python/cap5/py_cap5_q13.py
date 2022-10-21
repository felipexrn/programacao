a, b, c = map(int, input().split())
dia = a >= 1 and a <= 31
mes = b >= 1 and b <= 12
ano = c >= 1
if dia and mes and ano:
  if b == 4 or b == 6 or b == 9 or b == 11:
    if a == 31:
      print("inválida")
    else:
      print("válida")
  elif b == 2:
    if a >= 29:
      print("inválida")
    else:
      print("válida")
  else:
    print("válida")
else:
  print("inválida")