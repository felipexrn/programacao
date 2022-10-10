a1, a2, a3, a4 = map(int, input().split())

def achaDivisores(numero):
  divisores = []
  for i in range(1,numero+1):
    if numero % i == 0:
        divisores.append(i)
  print(divisores)
  return divisores

divisoresA1 = achaDivisores(a1)
divisoresA2 = achaDivisores(a2)
divisoresA3 = achaDivisores(a3)
divisoresA4 = achaDivisores(a4)

a = set(divisoresA1)
b = set(divisoresA2)
c = set(divisoresA3)
d = set(divisoresA4)

interA = (a & b) | (a & c) | (a & d) 
interB = (b & a) | (b & c) | (b & d)
interC = (c & a) | (c & b) | (c & d)
interD = (d & a) | (d & b) | (d & c)

inter1 = (interA | interB | interC |interD) - (interA & interB & interC & interD)
inter2 = (interB | interC |interD) - (interB & interC & interD)
inter3 = (interC |interD) - (interC & interD)
print (inter1)
print (inter2)
print (inter3)

print(interA)
print(interB)
print(interC)
print(interD)
'''
if :
  print("S")
else:
  print("N")
'''
"""
Entrada
1 2 4 8
Saída
S
	
Entrada
1 2 3 4
Saída
N
	
Entrada
15 14 6 35
Saída
S
"""