n = int(input())
numeros = []
for a in range(n):
  num = int(input())
  if num != 0:
    numeros.append(num)
  else:
    numeros.pop()
print(sum(numeros))

'''

Entrada
4
3
0
4
0
Saída
0
	
 

Entrada
10
1
3
5
4
0
0
7
0
0
6
Saída
7
	
'''