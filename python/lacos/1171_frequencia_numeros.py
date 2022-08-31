n = int(input())
numeros = []
quantidade = []
resposta = []
teste = []
for i in range(n):
  x = int(input())
  try:
    quantidade[numeros.index(x)] += 1
  except:
    numeros.append(x)
    quantidade.append(1)

for i in range(len(numeros)):
  resposta.append([numeros[i], quantidade[i]])
resposta.sort()

for i in resposta:
  print(i[0], "aparece", i[1], "vez(es)")

'''
Casos de teste:
Entrada:
7
8
10
8
260
4
10
10

Saída:
4 aparece 1 vez(es)
8 aparece 2 vez(es)
10 aparece 3 vez(es)
260 aparece 1 vez(es)

'''
