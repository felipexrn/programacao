# resolvido 100% 

pico = 0
while int(input()) != 0:  
  h = list(map(int, input().split()))
  if len(h) == 2:
    pico = 2
  elif len(h) == 1:
    pico = 1
  else: #adição dos dois primeiros elementos da amostra 
    h.append(h[0])
    h.append(h[1])
  
  di = h[0] < h[1]
  if di:
    direcao = 0
  else:
    direcao = 1
    
  for i in range(len(h)):
    if i < len(h)-1:
      if (h[i] > h[i+1] and direcao == 0) or (h[i] < h[i+1] and direcao == 1):
        pico += 1
        direcao = 1-direcao
    
  print(pico)
  pico = 0

'''
Casos de teste
Entrada:
2
1 -3
6
40 0 -41 0 41 42
4
300 450 449 450
0

Saída:
2
2
4
'''
