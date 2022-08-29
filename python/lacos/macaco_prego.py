teste = 1 # Contador de testes
while True:
  n = int(input())
  if n == 0:
    break
  else:
    x1 = []
    x2 = []
    y1 = []
    y2 = []
    for i in range(n): # Lê os retangulos e armazena os valores de x e y
      rec = list(map(int, input().split()))
      x1.append(rec[0])
      x2.append(rec[2])
      y1.append(rec[1])
      y2.append(rec[3])

  intersecao_x = [max(x1), min(x2)] # Seleciona o valor de x do retâgulo mais à direita e o valor de x do retângulo mais baixo
  intersecao_y = [min(y1), max(y2)] # Selecioma o valor de y do retângulo mais abaixo e o y do retângulo mais curto
  
  if intersecao_x[0] < intersecao_x[1] and intersecao_y[0] > intersecao_y[1]: #Verifica se há intersecção
    print("Teste", teste)
    print(intersecao_x[0], intersecao_y[0], intersecao_x[1], intersecao_y[1]) # imprime o retângulo da intersecção
    print()
  else: # imprime quando não tem intersecção
    print("Teste", teste)
    print("nenhum")
    print()
  teste += 1
  
#100
'''

3
0 6 8 1
1 5 6 3
2 4 9 0
3
0 4 4 0
3 1 7 -3
6 4 10 0
0

Teste 1
2 4 6 3


Teste 2
nenhum
'''