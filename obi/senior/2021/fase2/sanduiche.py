n, m = map(int, input().split())
restricoes = []
for a in range(m):
  restricoes.append(list(map(int, input().split())))
combinacoes = 2**n-1
restricoes = 2**(n-m-1)
if m==0:
  print(combinacoes)
else:
  print(combinacoes - restricoes)

'''
1 2 3 4
1234
123
234
341
412
12
13
14
23
24
34
1
2
3
4


1 2 3
123
12
13
23
1
2
3

1 2
12
1
2


Entrada
3 2
2 3
1 2
Saída
4
	
 

Entrada
3 0
Saída
7
	
 

Entrada
3 3
1 2
2 3
1 3
Saída
3
	

'''