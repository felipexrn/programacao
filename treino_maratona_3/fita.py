n = int(input())
fita = list(map(int, input().split()))

fita_colorida = []
while len(fita) > 0:
  if fita[0] != 0:
    if fita.count(0) > 0:
      ponto_corte = fita.index(0)
      tira = fita[:ponto_corte + 1]
      fita = fita[ponto_corte + 1:]
    else:
      tira = fita.copy()
      fita = []
  else:
    tira = fita[0]
    fita_colorida.append(tira)
    fita = fita[1:]
  print(tira)
'''
8
-1 -1 0 -1 -1 -1 0 -1
'''