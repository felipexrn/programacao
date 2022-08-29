for n in range(1, 100):
  valor = n**2 + n + 41
  for i in range(1, 50):
    if valor % i == 0 and valor != i and i != 1 and n > 1:
      print(valor, "Não é primo, pois é divisível por", i, "e", valor // i)