terrenos = []

def area_terreno(largura, profundidade):
  return largura * profundidade

def le_linha(contador):
  global terrenos
  if contador > 0:
    lista = list(map(int, input().split()))
    terrenos.append(area_terreno(lista[0],lista[1]))
    le_linha(contador - 1)
    
le_linha(4)

indice = terrenos.index(max(terrenos))
if indice == 0:
  terreno_maior = "A"
elif indice == 1:
  terreno_maior = "B"
elif indice == 2:
  terreno_maior = "C"
elif indice == 3:
  terreno_maior = "D"

print(terreno_maior)



'''
10 20
20 30
30 25
20 15
C

14 18
14 12
12 15
12 20
A

10 24
12 22
14 20
16 18
D
'''