# resolvido 100%

while True:
  n, m = map(int, input().split()) # lê a entrada
  if n == m == 0: # para a leitura e encerra o programa
    break 
  else:
    t = list(map(int, input().split())) # lista de bilhetes
    contador = 0
    if n > m: # sei lá porque... mas armazenei se tiveram mais bilhetes ou mais pessoas 
      m = n
    for i in range(1,m+1):
      try:
        if t.count(i) > 1: # verifica quantos bilhetes de cada bilhete existe na lista
          contador += 1
      except:
        pass 
    print(contador)

'''
Casos de teste
Entrada
5 5
3 3 1 2 4
6 10
6 1 3 6 6 4 2 3 1 2
0 0

Saída
1
4

'''
