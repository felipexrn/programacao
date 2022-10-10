# resolvido 100%

n, c, m = map(int, input().split())
x = list(map(int, input().split()))
y = list(map(int, input().split()))
for i in x:
  if y.count(i) > 0: # conta a quantidade de figurinhas especiais que existem
    c -= 1 
print(c)

'''
Casos de teste
Entrada:
10 2 5
4 7
7 1 2 8 3
Saída
1

Entrada
10 2 6
4 7
7 1 8 4 9 3
Saída
0

Entrada
8 4 10
2 4 6 8
3 1 1 5 1 1 7 7 1 1
Saída
4
'''
