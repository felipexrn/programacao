def troca(lista): # troca itens da lista
  primeiro = lista[0]
  del lista[0]
  lista.append(primeiro)
  return lista

n = int(input())
podium = []
paises = []

for i in range(n): # lê a entrada
  pais = list(input().split())
  podium.append(pais)

podium.sort(reverse = True) # ordena por ordem alfabética
#podium.reverse() # ordena por ordem alfabética (para comparação numérica)

for i in range(len(podium)):
  pais = podium[i]
  paises.append(pais[0]) # reserva os nomes dos paises
  pais[0] = i
  for j in range(4): # converte números de medalhas para int
    pais[j] = int(pais[j])

#print(*podium)
for j in podium:
  pais = j
  pais = troca(pais)
podium.sort(reverse = True) # ordena medalhas de ouro
#podium.reverse()

resultado = []

for i in range(len(podium)): #ordena demais medalhas (Sabe-se lá como)
  try:
    pais_atual = podium[i]
    pais_seguinte = podium[i+1]
    for j in range(4):
      if pais_atual[j] > pais_seguinte[j]:
        resultado.append(pais_atual)
        break
      else:
        pass
  except:
    resultado.append(pais_seguinte)

for i in range(len(resultado)): # colocar o nome do pais novamente no lugar
  pais = resultado[i]
  ultimo = pais[len(pais)-1]
  del pais[len(pais)-1]
  pais.reverse()
  pais.append(ultimo)
  pais.reverse()
  pais[0] = paises[pais[0]]
  print(*resultado[i])

'''
8
Belgica 2 2 2
Brasil 7 6 6
Franca 10 18 14
Italia 8 12 8
Australia 8 11 10
Colombia 3 2 3
Suica 3 2 2
Tailandia 2 2 2

Franca 10 18 14
Italia 8 12 8
Australia 8 11 10
Brasil 7 6 6
Colombia 3 2 3
Suica 3 2 2
Belgica 2 2 2
Tailandia 2 2 2

'''