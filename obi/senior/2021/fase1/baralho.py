naipe = ["C", "E", "U", "P"]
baralho = []
for a in naipe:
  for b in range(13) :
    baralho.append(str("{:02d}".format(b + 1)) + a)
# print(baralho)
cartas = input()
qtd_cartas = len(cartas)
cartas_impressas = []
for i in range(qtd_cartas // 3):
  cartas_impressas.append(cartas[:3])
  cartas = cartas[3:]
# print(cartas_impressas)
exibicao = [13, 13, 13, 13]
for a in baralho:
  contador = 0
  for b in cartas_impressas:
    if a == b and contador == 0:
      carta = a
      carta = carta[2:]
      for c in naipe:
        if c == carta and exibicao[naipe.index(c)] != "erro":
          exibicao[naipe.index(c)] -= 1
      contador += 1
    elif a == b and contador > 0:
      carta = a
      carta = carta[2:]
      for d in naipe:
        if d == carta:
          exibicao[naipe.index(d)] = "erro"
print(exibicao[0])
print(exibicao[1])
print(exibicao[2])
print(exibicao[3])


