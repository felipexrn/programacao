n, m = map(int, input().split())
nPais = list(map(int, input().split()))
mFesta = list(map(int, input().split()))
geracoes = [[0]]
geracao = []
contador = 0
for h in range(0, len(nPais)):
  contador = 0
  for i in range(0, len(nPais)):
    contador += 1
    lista = geracoes[len(geracoes) - 1]
    for j in lista: 
      if nPais[i] == j:
        geracao.append(contador)
  if len(geracao) > 0:  
    geracoes.append(geracao)
  geracao = []
geracoes = geracoes[1:]
porcentagem = []
for k in geracoes:
  contador = 0
  total = len(k)
  for l in range(0, len(mFesta)):
    for m in k:
      if m == mFesta[l]:
        contador += 1
  presente = contador
  porcentagem.append("{:.2f}".format(presente / total * 100))    
print(*porcentagem)