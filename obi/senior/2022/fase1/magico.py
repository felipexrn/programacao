n = int(input())
quadrado = []
for a in range(n):
  l = list(map(int, input().split()))
  quadrado.append(l)
lista = []
maximo = 0
numero = 0
linha = 0
coluna = 0
for b in quadrado:
  soma = sum(b)
  lista.append(soma)
  maximo = max(lista)
  linha = lista.index(min(lista)) + 1
c = quadrado[linha - 1]
coluna = c.index(0) + 1
numero = maximo - sum(quadrado[linha - 1])
print(numero)
print(linha)
print(coluna)
