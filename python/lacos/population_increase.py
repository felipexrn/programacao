t = int(input())
dados = []

for i in range(t):
  dados = list(input().split())
  for i in range(len(dados)//2):
    dados[i] = int(dados[i])
    dados[i+2] = float(dados[i+2])
    
  tempo = 0;
  while dados[0] <= dados[1]:
    if tempo <= 100: # veirificar se passaram mais de 100 anos
      pa = float(dados[0])
      pb = float(dados[1]) 
      g1 = dados[2]
      g2 = dados[3]
      pa += pa * g1 // 100
      pb += pb * g2 // 100
      dados[0] = int(pa)
      dados[1] = int(pb)
      tempo += 1
    else:
      break
  if tempo <= 100:
    print(tempo, "anos.")
  else: 
    print("Mais de 1 seculo.") #para todos os casos de mais de 100 anos
#100%

'''

6
100 150 1.0 0
90000 120000 5.5 3.5
56700 72000 5.2 3.0
123 2000 3.0 2.0
100000 110000 1.5 0.5
62422 484317 3.1 1.0

51 anos.
16 anos.
12 anos.
Mais de 1 seculo.
10 anos.
100 anos.

'''