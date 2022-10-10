#programa para verificar se uma lista é ordenada

#leitura de dados
l = list(map(int, input().split()))

#função para verificar se uma lista é ordenada
def ordem(l, i):
  maiorIgual = True
  if i > 0:
    iN = len(l)-1
    iA = iN-1
    if not l[iN] >= l[iA]:
      maiorIgual = False
    else:
      return ordem(l[:iN], i-1)
  return maiorIgual

#gatilho do programa e exibição de dados
print(ordem(l, len(l)))


'''
1 2 3
3 2 1
1 1 1
1 3 2
2 1 3
'''