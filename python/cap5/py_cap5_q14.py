a, b, c = map(int, input().split())
validade = a >= 1 and a <= 31 and b >= 1 and b <= 12 and c >= 1
mes30 = b == 4 or b == 6 or b == 9 or b == 11
if validade and ((mes30 and a <= 30) or (b == 2 and a <= 28) or a <= 31):
  a += 1
  if b == 2 and a == 29:
    a = 1
    b = 3
  elif mes30 and a == 31:
    a = 1
    b += 1
  else:
    if a == 32:
      a = 1
      b += 1
  if b == 13:
    b = 1
    c += 1
  print("{:02d}".format(a),"{:02d}".format(b),c, sep = "/")
else:
  print("data inválida")