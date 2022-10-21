n = int(input())
l = list(map(int, input().split()))
palindromo = False
operacoes = 0
debug = False
def separaLista():
  global l
  tamanho = len(l) // 2
  metade1 = []
  metade2 = []
  if len(l) % 2 == 0:
    metade1 = l[: tamanho]
    metade2 = l[tamanho :]
    metade2.reverse()
  else:
    metade1 = l[: tamanho]
    metade2 = l[tamanho + 1 :]
    metade2.reverse()
  return metade1, metade2
  
def verificaLista(l):
  global palindromo
  metade1, metade2 = separaLista()
  if metade1 == metade2:
    palindromo = True
  else:
    palindromo = False
  if debug:
    print("A lista é palíndroma", palindromo)
  return palindromo

def contracao():
  global l, operacoes
  contador = -1
  item1 = 0
  for b in l:
    verificaLista(l)
    if palindromo:
      if debug:
        print(l)
      break
    else:   
      if contador >= len(l) // (- 2):
        if l[item1] != l[contador]:
          if debug:
            print(l[item1], "e", l[contador], "são difetentes e opostos")
          pos_b = contador * (-1)
          ant_c = contador - 1
          if l[item1] > l[contador]:
            l[contador] += l[ant_c]
            del l[ant_c]
            operacoes += 1
          else:
            l[pos_b - 1] += l[pos_b]
            del l[pos_b]
            operacoes += 1
        else:
          if debug:
            print("Os itens",l[item1] , "e", l[contador],"são iguais")
        if l[item1] == l[contador]:
          contador -= 1
          item1 += 1
      if debug:
        print("O contador é", contador)
    if debug:
      print(l)
      
for c in l:
  if palindromo == False:
    contracao()
  else:
    break
print(operacoes)
#50%
'''

Entrada
5
10 60 20 40 10
Saída
1

Entrada
5
999 1 999 1 999
Saída
0

Entrada
4
10 40 30 20
Saída
2

Entrada
10
0 1 2 4 7 3 1 2 0 1
Saída
3

Entrada
5
998 2 999 1 999
Saída
2

Entrada
1
1
Saída
0

Entrada
20
0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9
Saída
17

Entrada
4
10 40 50 100
Saída
2

Entrada
11
10 40 50 100 20 90 10 40 30 2 28
Saída
6

Entrada
20
0 1 2 3 4 5 6 7 8 9 9 8 7 6 5 4 3 2 0 1
Saída
2

Entrada
6
1 2 3 3 1 7
Saída
?

'''