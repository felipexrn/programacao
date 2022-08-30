j, r = map(int, input().split())
jogadores = []
rodadas = []

for i in range(j):
  jogadores.append(0)
rodadas = list(map(int, input().split())) # Lê os pontos dos jogadores nas rodadas

for i in range(j):
  for k in range(r):
    jogadores[i] += rodadas[(j*k)+i] # verifica os pontos de cada jogador
    
maior = max(jogadores) # seleciona a maior pontuação 

for i in range(j):
  if jogadores[j-1-i] == maior: # encontra qual jogador é o ganhador
    ganhador = j-i
    break

print(ganhador)

'''
Amostras de entrada	Amostras de saída
3 3
1 1 1 1 2 2 2 3 3
3

2 3
0 0 1 0 2 0
1

'''