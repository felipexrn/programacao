def fluxo(n, tempo, direcao):

  #entrada de dados para submissão
  '''
  n = int(input())
  tempo = []
  direcao = []
  for a in range(n):
    t, d = map(int, input().split())
    tempo.append(t)
    direcao.append(d)
  
  '''
  curso = True
  
  if curso:
    e = False
    t = 0
    d = 0

    for a in range(n):
      if t < tempo[a]:
        if not e:
          t = tempo[a] + 10
          d = direcao[a]
      else:
        if d == direcao[a]:
          t = tempo[a] + 10
          d = direcao[a]
        else:
          e = True
      if e:
        if t >= tempo[a] +10:
          e = False
          t += 10
          if d == 0:
            d = 1
          else:
            d = 0
        elif t < tempo[a]:
          e = False
          t += 10
          if d == 0:
            d = 1
          else:
            d = 0
          
          
    return t
    
  else:
    if len(tempo) > 0:
      subir = 0
      descer = 0
    for b in range(len(tempo)):
      if b == 0:
        if direcao[b] == 0:
          subir = tempo[b] + 10
        else:
          descer = tempo[b] + 10
      elif b < len(tempo) -2:
        #só uma direção
        if direcao[b] == direcao[b-1] and direcao[b] == 0:
          if tempo[b] != tempo[b-1]:
            subir = tempo[b] + 10
        elif direcao[b] == direcao[b-1] and direcao[b] == 1:
          if tempo[b] != tempo[b-1]:
            descer = tempo[b] + 10
            
        #tá subindo e vai descer
        elif direcao[b] != direcao[b-1] and direcao[b] == 1:
          if direcao[b+1] != direcao[b] and tempo[b+1] <= subir:
            if tempo[b] > subir and tempo[b] > descer:
              descer =  tempo[b] - abs(subir-descer) + 10
            elif tempo[b] <= subir and tempo[b] <= descer:
              descer = tempo[b] + 10
            elif tempo[b] <= subir and tempo[b] > descer:
              descer += 10
            elif tempo[b] > subir and tempo[b] <= descer:
              descer = subir - tempo[b] + 10
            elif tempo[b] > subir and tempo[b] > descer:
              descer = tempo[b] + 10
  
        #tá descendo e vai subir
        elif direcao[b] != direcao[b-1] and direcao[b] == 0:
          if tempo[b] > descer and tempo[b] > subir:
            subir = tempo[b] - abs(subir-descer) + 10
          elif tempo[b] <= descer and tempo[b] <= subir:
            subir = tempo[b] + 10
          elif tempo[b] <= descer and tempo[b] > subir:
            subir += 10
          elif tempo[b] > descer and tempo[b] <= subir:
            subir = descer - tempo[b] + 10
          elif tempo[b] > descer and tempo[b] > subir:
            subir = tempo[b] + 10
      else:
        if direcao[b] == direcao[b-1] and direcao[b] == 0:
          aff = 0
        elif direcao[b] == direcao[b-1] and direcao[b] == 1:
          oxe = 0 
            
    return subir + descer

'''
Exemplo de entrada 1
3
5 0
8 0
13 0
Exemplo de sa´ıda 1
23
Exemplo de entrada 2
3
5 0
7 1
9 0
Exemplo de sa´ıda 2
29
Exemplo de entrada 3
3
5 0
10 1
16 0
Exemplo de sa´ıda 3
35
'''
