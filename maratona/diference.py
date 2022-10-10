t = int(input())
n = []

for a in range(t):
  tl = int(input())
  lista = list(map(int, input().split()))
  n.append(lista)

for b in n:
  resposta = "yes"
  for c in b:
    if c%b[0]!=0:
      resposta = "no"
      break
  print(resposta)
  