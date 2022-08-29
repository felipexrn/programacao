resultados = []
for a in range(6):
  resultados.append(input())
vitorias = resultados.count("V")
if vitorias >= 5:
  print(1)
elif vitorias >= 3:
  print(2)
elif vitorias >= 1:
  print(3)
else:
  print(-1)

'''

Entrada
V
V
P
P
P
V
Saída
2

Entrada
P
P
P
P
P
P
Saída
-1
	
'''