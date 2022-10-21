r = int(input())
registros = []
amigos = []
tempo_total = 0
tempo = 0
envios = 0
recebidas = 0
for a in range(r):
  registros.append(input().split())
for b in registros:
  lista = b
  if lista[0] != "T":
    amigos.append(lista[1])
amigos = list(set(amigos))
for c in amigos:
  contador = 0
  for d in registros:
    lista = d
    if lista[0] == "T":
      tempo += int(lista[1])
      contador += 1
    else:  
      if contador > 0:
        regAnt = registros[contador - 1]
        if regAnt[0] != "T":
          if lista[0] == "E":
            if lista[1] == c:
              envios += 1
              tempo_total += tempo + 1
              tempo = 0
            else:
              tempo += 1 
          elif lista[0] == "R":
            if lista[1] == c:
              recebidas += 1
              tempo = 0
            else:
              tempo += 1
        else:
          if lista[0] == "E":
            if lista[1] == c:
              envios += 1
              tempo_total += tempo
              tempo = 0
          elif lista[0] == "R":
            if lista[1] == c:
              tempo = 0
              recebidas += 1
        contador += 1
      elif contador == 0:
        if lista[0] == "E" and lista[1] == c:  
           envios += 1
        elif lista[0] == "R" and lista[1] == c:
         recebidas += 1
        contador += 1
  if envios == recebidas:
    amigos[amigos.index(c)] += " " + str(tempo_total)
  else:
    amigos[amigos.index(c)] += " " + "-1"
  tempo = 0
  tempo_total = 0
  envios = 0
  recebidas = 0
amigos.sort()
for e in amigos:
  print(e)
'''

Entrada
5
R 2
R 3
T 5
E 2
E 3

Saída
2 6
3 6
	

Entrada
14
R 12
T 2
R 23
T 3
R 45
E 45
R 45
E 23
R 23
T 2
E 23
R 34
E 12
E 34

Saída
12 13
23 8
34 2
45 -1
'''