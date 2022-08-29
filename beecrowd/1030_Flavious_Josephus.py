nc = int(input())
for i in range(nc):
  n, m = map(int, input().split())
  roda = []
  for j in range(n):
    roda.append(j+1)
  while roda.count(0) > 1:
    try:
      if roda[roda.index(m+(k*m))] == m:
        
    except:
      roda[roda.index(m+(k*m))] = 0
  print(f"Case {i+1}: {max(roda)}")
'''
1 2 3 4 5


3
5 2
6 3
1234 233

Case 1: 3
Case 2: 1
Case 3: 25
'''