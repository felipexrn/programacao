n = int(input())
p = input()
anagrama1 = p[:n//2]
anagrama2 = p[n//2:]
erro = False
diferente = False
for a in anagrama2:
  try:
    anagrama1.index(a)
  except ValueError:
    print("*")
    erro = True
    break
for a in p:
  if p[0] != a:
    diferente = True
    break
if not diferente:
  print(p[0])
if not erro and diferente:
  print(anagrama1)

#?% problema no servidor de testes

'''

Entrada
5
xxxxx
Saída
x
	

Entrada
2
xy
Saída
*
	

Entrada
6
bbabab
Saída
bba

'''