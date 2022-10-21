total = float(input())
conta = total
if total>=100.0:
  conta = conta-0.1*total
  print("A")
elif total>=200.0:
  conta = conta-0.2*total
  print("B")
elif total>=300.0:
  conta = conta-0.3*total
  print("C")
elif total>=400.0:
  conta = conta-0.4*total
  print("D")
elif total>=500.0:
  conta = conta-0.5*total
  print("E")
print("{:.2f}".format(conta))