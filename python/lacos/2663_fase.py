# resolvido 100%

n = int(input())
k = int(input())
p = []

for i in range(n):
  p.append(int(input())) # lê os dados

p.sort() # ordena a lista
p.reverse() # inverte a lista
ultimo = p[k-1] # seleciona a pontuação do último colocado
p.reverse() # inverte a lista
p = p[p.index(ultimo):] # procura a primeira ocorrencia da pontuação do último colocado

print(len(p)) # imprime quantos foram classificados

'''
Casos de teste:
Entrada:
10
3
1
2
3
4
5
5
4
3
2
1

Sáida:
4

Entrada:
5
2
500
500
500
500
500

Saída:
5

'''
