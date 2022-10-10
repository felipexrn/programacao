# resolvido 100% 

fim = False
while not fim:
  h = list(map(int, input().split()))
  if sum(h) == 0:
    fim = True
  else:
    if h[0] == h[2]: # mesma hora
      if h[1] == h[3]: # mesmo minuto
        tempo = 1440
      elif h[1] > h[3]: # passaram 23 horas e falta pouco pra completar um hora cheia
        tempo = 1440 - ((h[0]*60) + h[1]) + (h[2]*60 + h[3])
      else: 
        tempo = h[1] - h[3] # passaram minutos
        
    elif h[0] > h[2]: # passou das 00:00
      if h[1] == h[3]: # mesmo minuto
        tempo = 1440 - (h[0] - h[2]) * 60
      elif h[1] > h[3]: # falta pouco pra completar uma hora cheia
        tempo = 1440 - ((h[0]*60) + h[1]) + (h[2]*60 + h[3])
      else:
        tempo = ((h[0]*60) + h[1]) - (1440 + (h[2]*60 + h[3])) # passaram minutos 
        
    else: # passaram horas
      if h[1] == h[3]: # mesmo minuto
        tempo = (h[0] - h[2]) * 60
      elif h[1] > h[3]: # falta pouco pra completar uma hora cheia
        tempo = (h[0]*60 + h[1]) - (h[2]*60 + h[3])
      else:
        tempo = (h[0]*60 + h[1]) - (h[2]*60 + h[3]) # passaram minutos
        
    print(abs(tempo))


'''
Casos de teste:

Entrada:
1 5 3 5
23 59 0 34
21 33 21 10
0 0 0 0

Saída:
120
35
1417

Entrada:
23 27 1 59 
22 30 8 30
21 00 8 00
0 0 0 0

Saída:
152
600
660



'''
