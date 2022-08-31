nc = int(input())
for i in range(nc):
  n, k = map(int, input().split())
  roda=[]
  for j in range(n):
    roda.append(j+1)
  endereco = 0
  while len(roda) > 1:
    if k > len(roda):
      del roda[k+endereco-1]
      endereco += k-1 
    else: 
      endereco = abs(endereco-len(roda))
  print(f"Case {i+1}: {roda[sortudo]}")
'''
Casos de teste:

1 2 3 4 5
1 2 3 4

1 2 3 4 5
3 1   2 4  

1 2 3 4 5
2 4 1   3

1 2 3 4 5
  4 2 1 3

1 2 3 4 5
2   3 4 1

1 2 3 4 5
1 3 2   4

Entrada:
3
5 2
6 3
1234 233

Saída:
Case 1: 3
Case 2: 1
Case 3: 25
'''