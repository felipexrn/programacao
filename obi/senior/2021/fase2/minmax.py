s = int(input())
a = int(input())
b = int(input())
intervalo = list(range(a, b + 1))
somas = []
for a in intervalo:
  numero = str(a)
  algarismos = []
  for b in numero:
    algarismos.append(int(numero[0]))
    numero = numero[1:]
  soma = sum(algarismos)
  if s == soma:
    somas.append(int(a))
print(min(somas))
print(max(somas))
#100%
'''

Entrada
3
10
30
Saída
12
30
	
 

Entrada
12
100
500
Saída
129
480
	
 

Entrada
18
1
100
Saída
99
99

'''