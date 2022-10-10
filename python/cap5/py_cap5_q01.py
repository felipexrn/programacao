n1 = float(input())
n2 = float(input())
media = (n1 * 2 + n2 * 3)/5
if n1 >= 0.0 and n1 <= 10.0 and n2 >= 0.0 and n2 <= 10.0:
  if media >= 6.0:
    print("Aprovado")
  else:
    print("Em recuperação")
  print("{:.2f}".format(media))
else:
  print("Notas possuem valores inválidos")