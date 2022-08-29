jogadores = []
for a in range(4):
  jogadores.append(int(input()))
time1 = min(jogadores) + max(jogadores)
jogadores.remove(min(jogadores))
jogadores.remove(max(jogadores))
time2 = sum(jogadores)
if time1 - time2 >= 0:
  print(time1 - time2)
else:
  print(time2 - time1)
#100% 

'''


Entrada
4
7
10
20
Saída
7
	
 

Entrada
0
0
1
1000
Saída
999
	
 

Entrada
1
2
3
4
Saída
0
	

'''