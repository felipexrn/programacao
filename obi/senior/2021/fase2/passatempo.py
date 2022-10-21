lin, col = map(int, input().split())
matriz = []
linha = []
coluna = []
result_l = []
result_c = []
debug = False
variaveis = []
valores = []
exibicao = []
def printMatriz():
  for a in matriz:
    print(a, result_l[matriz.index(a)])
  print(result_c)

for a in range(lin):
  linha = input().split()
  result_l.append(int(linha[-1]))
  del linha[-1]
  matriz.append(linha)
result_c = list(map(int, input().split()))
linha = 0
coluna = 0

for b in matriz:
  l0 = b.copy()
  i0 = l0[0]
  string = True
  for c in l0:
    if type(c) == str:
      string = True
      if debug:
        print("type de", c, "é str")
    else:
      string = False
      if debug:
        print("type de", c, "é int")
  if string:
    igual = True
    for d in l0:
      if i0 == d:
        igual = True
      else:
        igual = False  
    if igual:
      valor = result_l[linha] // len(b)
      if len(valores) == 0:
        variaveis.append(l0[0])
        valores.append(valor)
      else:
        valores[variaveis.index(l0[0])] += valor
      for e in b:
        b[coluna] = valor
        coluna += 1 
      coluna = 0
  else:
    sum_l = 0
    l1 = b.copy()
    i1 = l1[coluna] 
    for f in l1:
      if type(f) == int:
        sum_l += f
        del l1[coluna]
        if debug:
          print("sum_l", sum_l)
      coluna += 1
    coluna = 0
    if sum_l != result_l[linha]:
      igual = True
      for g in l1:
        if debug:
          print("l1", l1)
          print("i1 da l1", l1[0], "item da coluna", coluna,"=", g)
        if l1[0] == g:
          igual = True
        else:
          igual = False
      if igual:
        valor = result_l[linha] // len(l1) - sum_l
        if len(valores) == 0:
          variaveis.append(l1[0])
          valores.append(valor)
        try:
          valores[variaveis.index(l1[0])] += valor
        except ValueError:
          variaveis.append(l1[0])
          valores.append(valor)
        for h in b:
          b[coluna] = valor
          coluna += 1
        coluna = 0
  for i in range(len(variaveis)):
    for j in matriz:
      l2 = j.copy()
      i2 = l2[coluna]
      if i2 == variaveis[i]:
        j[coluna] = valores[i]
      coluna += 1
    coluna = 0
  if debug:
    print("Contador de linha",linha)
    print("Contador de coluna",coluna)
  linha += 1
linha = 0


if debug:
  printMatriz()

for x in range(len(variaveis)):
  exibicao.append(variaveis[x] + " " + str(valores[x]))
exibicao.sort()

for y in range(len(variaveis)):
  print(exibicao[y])
#0%
'''

Entrada
2 2
aa aa 2
zz aa 3
3 2 
Saída
aa 1
zz 2

Entrada
4 5
df bb cg df df 11
ee az cg az ee 6
df cg cg df df 10
az az cg az az 6
6 7 8 6 6
Saída
az 1
bb 3
cg 2
df 2
ee 1
	

Entrada
3 4
aa bb cc dd 10
aa bb cc dd 10
aa bb cc dd 10
3 6 9 12
Saída
aa 1
bb 2
cc 3
dd 4
	

Entrada
3 3
aa zz aa 27
vv zz aa -5
kk kk aa 40
15 -7 54
Saída
aa 18
kk 11
vv -14


'''