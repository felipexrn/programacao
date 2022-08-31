# resolvido 100%

n = int(input())
v = []
sequencia = 0
for i in range(n):
  v.append(int(input()))  # lê os dados
for i in range(len(v)):
  try:
    if v[i] != v[i+1]: # verifica se o próximo item é diferente do atual 
      sequencia += 1
  except:
    sequencia += 1
print(sequencia)

'''
Casos de teste
Entrada
5
1
1
1
2
1
Saída
3

Entrada
12
1
2
1
2
2
2
1
1
2
2
1
1
Saída
7

Entrada
3
1
2
1
Saída
3
