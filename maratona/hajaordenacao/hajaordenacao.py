curso = True

if curso:
  n, k = map(int, input().split())
  cores_ordenadas = []
  cores = []

  #otimização de algoritmo na leitura de dados
  for a in range(n):
    cores_ordenadas.append(0)
  
  for b in range(n):
    cubo, cor = map(int, input().split())
    cores.append(cor)
    cores_ordenadas[cubo-1] = cor
  
  possivel = True
  
  for c in range(n):
    if cores_ordenadas[c] != cores[c]:
      possivel = False
      break
      
  #print(cores)
  #print(cores_ordenadas) 
  
  if possivel:
    print("Y")
  else:
    print("N")
  
'''

Exemplo de entrada 1
4 2
3 1
4 2
1 1
2 2
Exemplo de saída 1
Y
Exemplo de entrada 2
4 2  
2 1
4 2
1 1
3 2
Exemplo de saída 2
N
Exemplo de entrada 3
3 1
1 1
2 1
3 1
Exemplo de saída 3
Y
input/H_27
10 4
3 4
6 3
1 1 
5 2
4 3
7 2
10 4
9 3
2 4
8 3
output/H_27
N
'''