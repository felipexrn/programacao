n = int(input())
votos = []
for i in range(n):
  votos.append(int(input()))
ganhador = max(votos)
if votos[0] == ganhador:
  print("S")
else:
  print("N")